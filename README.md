# dwm (Data Washing Machine)
Red Hat's business logic for maintaining marketing data quality

# Introduction

Database quality is a problem for many companies. Often there is a mad dash to collect as much data as possible before a single thought is given to keeping that data high quality. Some examples of bad input data include:

 - Data collection tools (such as interest or freemium forms) that require manual input, rather than OAuth or picklists
 - Ill-trained data entry or office staff
 - Data purchased from outside sources that does not conform with company standards

Bad data introduced through these sources can lead to significant amounts of lost time invested in manual correction, or directly to lost opportunities and revenue due to not being able to query on clean data. Obviously, one solution is to make sure that all data collection sources conform with your database standards, but if you can make that happen, then I'll just be over here flying on my unicorn.

This package was originally developed for use by Red Hat's Marketing Operations group to maintain quality of contact data, although the principles are sound enough to apply to many types of databases.

# Business logic

The following are what we have determined to be (as a best practice) the general rules available for cleaning a set of data. Theoretically, any string field can have these rules applied to them; however, when configuring DWM, one should evaluate whether or not a rule is appropriate for a given field.

## Validation

Validation is the removal of data that is straight-up junk and provides no business value whatsoever. This data is usually the result of spam-bots, errors in collection tools (such as posting bad html strings), or someone uploading the wrong spreadsheet. We've split validation into two pieces: generic and field-specific.

### Generic

Generic validation is the removal of data that has no place in a given database, no matter what field it is found in. The following are examples of generic bad data:

```
aaaaaaaaaaaaaaa ## one repeated character
fdsafdasfdfdsafdafdsa ## all typed with left hand on the home line
buy levitra cialis ## spam data
www.buymystuff.com ## marketing database-specific example; our processes do not try to clean any website/URL related fields, so if this appears in one of the fields we are cleaning, it's probably bad data
```

DWM uses two types of generic validation:

- `genericLookup`: remove 'bad' values based on a known list of bad data (previously observed)
- `genericRegex`: remove 'bad' values based on regular expressions; i.e., any word longer than 4 characters which is all the same character; or a string containing 'viagra'

### Field-Specific

Field-Specific validation is the removal of data that is junk in one field, but good data in another. An example is a string of nine numbers: ```9493020093```. In a phone number field, this is probably good data. In the First Name field, it's junk. Conversely, ```hi, this is a string of letters``` may have a purpose in a text-based field, but it provides no reasonable data in a phone number field.

DWM uses two types of field-specific validation:

- `fieldSpecificLookup`: remove 'bad' values based on a known list of bad data (previously observed)
- `fieldSpecificRegex`: remove 'bad' values based on regular expressions; i.e., for the field `firstName`, remove any value containing all numbers

## Normalization

Normalization is the correction of data to conform with a certain expected set of values. For example, `Proggrrammer/Developer` is almost a valid "Job Role" value `Programmer/Developer`, but is mis-spelled. Another example is `Programmer`, which obviously would fall into the previous category, but is not an exact value match.

Note that normalization usually cannot be applied to fields that are expected to be free-text, such as "First Name" or "Company Name". If certain rules need to be applied to those fields, use of the __User-Defined Functions__ is recommended.

DWM uses two types of normalization:

- `normLookup`: replace 'almost' values based on a known list of data (previously observed); i.e., common mis-spellings
- `normRegex`: replace 'almost' values based on regular expressions; i.e., for the field `jobRole`, replace any value that contains `programmer` but not `manager` with `Programmer/Developer`

## Derivation

Derivation is the management of fields designed to help business users more easily make decisions, but are not explicitly collected. One example is a "Super Region" field. Although "Country" is a value that is likely collected, users of the database may only need to filter to a general region to do their jobs.

DWM uses three types of derivation:

- `deriveValue`: given input values from one or more fields, find the corresponding output value; i.e., for `jobRole='Manager'` and `department='IT'`, then set `persona='IT Decision Maker'`
- `copyValue`: given an input value from one field, copy that value to the target field
- `deriveRegex`: given an input value from one field, derive target field value using regular expressions

Within the runtime configuration, derivation rules are ordered within a dictionary to maintain rule-hierarchy. So, if Rule 1 does not yield a result, then Rule 2 would be tried. The process will exit after one of the derivation rules produces a new value.

## User-Defined Functions

The above three processes are the most common processes that need to be applied to data, but not everything can be planned for. User-Defined functionality is designed to fill this gap. For instance, US Zipcodes can have some fairly basic and consistent transformations applied to make the data easier to work with (i.e., strip off trailing hypen/number combos, left pad with 0s in case of bad spreadsheet formatting), but those rules don't fall into any of the above categories.

Also included may be third-party data enrichment. For example, if you have an API contract with a company that provides IP address geolocation, or provides additional company info based on email domain, you can define a function to interact with that API and pull additional data into the fields of interest.

## Order

## Audit History

Record-level audit history is a record of what changes were made to which data fields. This includes what the previous value was, what the new/replacement value was, and what rule caused the change. The record is somewhat akin to a git commit, in that it only records where changes were made, and does not keep a record of anything that remained unchanged. Although it is optional in this package, it is recommended for any automation of these processes to provide both a record for troubleshooting and transparency for the business users of the database.

# Architecture

## Data Flow

![alt text](/diagrams/DWM_Arch_DataFlow.png "High-level flow of using the DWM")

1. Data is gathered for cleaning by the Python script utilizing the DWM package (i.e., using an API to export contact data from a Marketing Automation Platform)
2. Import custom functions (if applicable)
3. Connect to MongoDB using pymongo `MongoClient`
4. Data is passed (as a list of dictionaries), along with a `configName` and MongoDB connection, to the `dwmAll` function
5. Script takes post-processing action (i.e., using an API to import the cleaned data back into a Marketing Automation Platform)

## dwmAll

This function is the highest-level wrapper for all DWM functions.

![alt text](/diagrams/DWM_Arch_dwmAll.png "High-level flow of using dwmAll")

1. Use `configName` to retrieve config document from MongoDB
2. Apply sorting to relevant parts of config (`derive` and `userDefinedFunctions`)
  - Do this because you can't store a Python OrderedDict in MongoDB, and the order in which some rules are applied can be important
3. Loop through data, passing each record to `dwmOne` along with config and MongoDB collection
4. If configured to write history *and* return the history ID, append the `_id` to each record
5. Return list of dictionaries with cleaned data

## dwmOne

This function applies wrapper functions to each data record. It follows the specification above, in *Business Logic: Order*.

![alt text](/diagrams/DWM_Arch_dwmOne.png "High-level flow of using dwmOne")

1. Create a history collector `{}`
2. Run `userDefinedFunctions=beforeGenericValidation`
3. Run `lookupAll` with `lookupType='genericLookup'`
4. Run `userDefinedFunctions=beforeGenericRegex`
5. Run `lookupAll` with `lookupType='genericRegex'`
6. Run `userDefinedFunctions=beforeFieldSpecificValidation`
7. Run `lookupAll` with `lookupType='fieldSpecificLookup'`
8. Run `userDefinedFunctions=beforeFieldSpecificRegex`
9. Run `lookupAll` with `lookupType='fieldSpecificRegex'`
10. Run `userDefinedFunctions=beforeNormalization`
11. Run `lookupAll` with `lookupType='normLookup'`
12. Run `userDefinedFunctions=beforeNormalizationRegex`
13. Run `lookupAll` with `lookupType='normRegex'`
14. Run `userDefinedFunctions=beforeDeriveData`
15. Run `DeriveDataLookupAll`
16. Run `userDefinedFunctions=afterProcessing`
17. If `writeContactHistory==True`, write the history collector to the `contactHistory` collection in MongoDB
18. Return data record and history ID (if applicable, `None` otherwise)

## Wrapper functions

### `lookupAll`

### `DeriveDataLookupAll`

## Cleaning functions

## Helpers

# Setup Process

## Hosting

 - Local machine: it's entirely possible to run this complete process on your individual laptop/desktop, although may not recommended due to backup and business continuity risks.
 - PaaS: Platform-as-a-Service is the recommended route to get up-and-running quickly. This way, developers don't have to worry about the engineering concerns of making sure their services remain running. We're using Red Hat's Openshift, but there are other options (such as Heroku) available on AWS. Be warned that the PaaS may have to be internally hosted at your workplace to ensure connectivity to internal databases. You should also be aware of potential security concerns around PII, especially if you're storing record history, and may need to work with your IT team to ensure secure storage/transit for such data.

## Python

Python 2.7 is the recommended minimum, although a 3.x release is advisable if unicode support is required. This package is tested to work with Python 2.7, 3.3, 3.4, and 3.5.

## MongoDB

MongoDB is required for persistent storage of runtime configurations, lookup tables, regex rules, and derivation rules. It also serves as an (optional, but recommended) home for record-level audit history. Also, since operational data will be stored here, you should have some sort of routine backup process in place. Exact description of the schema is included in the DataDictionary.

This package was designed with MongoDB 3.2.x, but due to multi-key indexing requirements at least 2.5.5 is advised.

## Configuration

Runtime configuration for DWM is stored in a JSON document within MongoDB. It is retrieved by the unique "configName" field when the `dwmAll` function is called, and dictates which fields are cleaned, what types of lookups, regexes and derivation rules are called, and which user-defined functions should be called.
Multiple configurations can be stored and called for different purposes. For example, a configuration for use directly against a database may include rules for 20 fields, while one running within an API may only run against five fields.

Full example is given in the DataDictionary.md file.

__Required Fields:__

 - `configName`: Must be a unique string
 - `fields`: Includes a document for each field to be cleaned; each should include the following:
  * `lookup`: an array of which validation rules should be applied: `genericLookup, genericRegex, fieldSpecificLookup, fieldSpecificRegex, normLookup, normRegex`
  * `derive`: a document of documents, each named in order of execution (1,2,...) and containing the following sub-fields:
    * `type`: string indicating what type of derivation should be applied: `deriveValue, copyValue, deriveRegex`
    * `fieldSet`: array of field names to be used in derive process. Must contain only one value if `type==copyValue OR deriveRegex`.
    * `overwrite`: boolean indicating whether to write over an existing value
    * `blankIfNoMatch`: overwrite existing value with a blank value if no match found
 - `userDefinedFunctions`: document of the following sub-documents with ordered numeric names, indicating when user-defined functions should be run: `beforeGenericValidation, beforeGenericRegex, beforeFieldSpecificValidation, beforeFieldSpecificRegex, beforeNormalization, beforeNormalizationRegex, beforeDeriveData, afterProcessing`
 - `history`: settings dictating if/how to write contact history

## Lookups, Derivation, and Regex rules

A complete schema for these items is in the DataDictionary.md file. Also included is a recommendation for indexes to improve performance.

## User-Defined Functions

User-Defined functions must take exactly two inputs, `data` (a single dictionary of data to which transformations are applied) and `histObj` (a dictionary object used to record field-level changes), and output the same two (with changes applied to `data` and any relevant updates made to `histObj`). Helper functions for recording history are included in the dwm package.

UDFs should ideally be defined in a file separate from the script calling the DWM functions, then loaded in independently. If using UDFs, then the `dwmAll` parameter must be set `udfNamespace=__name__`

__Example:__

__udf.py__

```python
from dwm import _CollectHistory_, _CollectHistoryAgg_
def myFunction(data, histObj):

  fieldOld = data['myField']

  fieldNew = 'Hi! This is a data change'

  data['myField'] = fieldNew

  change = _CollectHistory_(lookupType='UDF-myFunction', fromVal=fieldOld, toVal=fieldNew) ## recommended format for lookupType: "UDF-nameOfFunction"

  histObjUpd = _CollectHistoryAgg_(contactHist=histObj, fieldHistObj=change, fieldName='myField')

  return data, histObj

```

__example.py__

```python
from dwm import dwmAll
from udf import myFunction

### get data to run through, define mongoDb collections and connection, etc

dataOut = dwm.dwmAll(data=data, mongoDb=db, mongoConfig=mongoConfig, configName='myConfig', returnHistoryId=False, udfNamespace=__name__)

```

# Examples

__Coming Soon: Red Hat's Marketing Operations implementation via Openshift__
