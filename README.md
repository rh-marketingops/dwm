# dwm (Data Washing Machine)
Red Hat's business logic for maintaining marketing data quality

# Introduction

Database quality is a problem for many companies. Often there is a mad dash to collect as much data as possible before a single thought is given to keeping that data high quality. Some examples of bad input data include:

 - Data collection tools (such as interest or freemium forms) that require manual input, rather than OAuth or picklists
 - Ill-trained data entry or office staff
 - Data purchased from outside sources that does not conform with company standards

Bad data introduced through these sources can lead to significant amounts of lost time invested in manual correction, or directly to lost opportunities and revenue due to not being able to query on clean data.

This package was originally developed for use by Marketing Operations groups to maintain quality of contact data, although the principles are sound enough to apply to many types of databases. It is built for use with MongoDB to allow easier creation of custom frontend UIs.

# Business logic

The following are what we have determined to be the general "best practices" for maintaining data quality.

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

### Field-Specific

Field-Specific validation is the removal of data that is junk in one field, but good data in another. An example is a string of nine numbers: ```9493020093```. In a phone number field, this is probably good data. In the First Name field, it's junk. Conversely, ```hi, this is a string of letters``` may have a purpose in a text-based field, but it provides no reasonable data in a phone number field.

## Normalization

Normalization is the correction of data to conform with a certain expected set of values. For example, `Proggrrammer/Developer` is almost a valid "Job Role" value `Programmer/Developer`, but is mis-spelled. Another example is `Programmer`, which obviously would fall into the previous category, but is not an exact value match.

Note that normalization usually cannot be applied to fields that are expected to be free-text, such as "First Name" or "Company Name". If certain rules need to be applied to those fields, use of the __User-Defined Functions__ is recommended.

## Derivation

Derivation is the management of fields designed to help business users more easily make decisions, but are not explicitly collected. One example is a "Super Region" field. Although "Country" is a value that is likely collected, users of the database may only need to filter to a general region to do their jobs.

## User-Defined Functions

The above three processes are the most common processes that need to be applied to data, but not everything can be planned for. User-Defined functionality is designed to fill this gap. For instance, US Zipcodes can have some fairly basic and consistent transformations applied to make the data easier to work with (i.e., strip off trailing hypen/number combos, left pad with 0s in case of bad spreadsheet formatting), but those rules don't fall into any of the above categories.

Also included may be thrid-party data enrichment. For example, if you have an API contract with a company that provides IP address geolocation, or provides additional company info based on email domain, you can define a function to interact with that API and pull additional data into the fields of interest.

# Architecture



## Cleaning Methods

### Lookups

Lookups utilize tables of expected values to apply to data cleaning with the above business logic. The advantage of lookups is fine-grained control over the definition of "bad data", as well as catching values that may not be consistently catchable with regular expressions. The disadvantage is that you have to manually create and update each lookup value.

### Regex

Regex applies consistent data cleaning rules. The advantages and disadvantages are the opposite of lookups; you can create fewer rules that require less maintenance, but you loose a lot of fine-grained control.

### Derivation Rules

Derivation includes both lookups and regex (with the same advantage/disadvantage split), but with the expectation of applying those to fields other than the target field.

__Example:__ Our marketing database has two roles related to a contacts' specific job, "Job Title" and "Job Role". "Job Title" was an free-text field on our legacy freemium/registration forms, and is still provided as an option for our marketers to upload to. "Job Role" is the current supported job info collection field on forms, and is a picklist of expected values. Since our segmentation processes require a "Job Role" value, we sometimes have to apply a derivation rule to get that value from "Job Title". In this case, if `Job Title == "Senior Applications Programmer"`, the result would be `Job Role == "Programmer/Developer"`. In this case, we are applying a derivation rule to the "Job Title" value to get a new "Job Role" value.

Within the runtime configuration, derivation rules are ordered within a dictionary to maintain rule-hierarchy. So, if Rule 1 does not yield a result, then Rule 2 would be tried. The process will exit after one of the derivation rules produces a new value.

## Audit History

Record-level audit history is a record of what changes were made to which data fields. This includes what the previous value was, what the new/replacement value was, and what rule caused the change. Although it is optional in this package, it is recommended for any automation of these processes to provide both a record for troubleshooting and transparency for the business users of the database.

## Data Flow

### dwmAll

### dwmOne

### Wrapper functions

# Setup Process

## Hosting

 - Local machine: it's entirely possible to run this complete process on your individual laptop/desktop, although is not recommended due to backup and business continuity risks.
 - PaaS: Platform-as-a-Service is the recommended route to get up-and-running quickly. This way, developers don't have to worry about the engineering concerns of making sure their services remain running. Options are Red Hat's Openshift, Heroku, and other options available on AWS. Be warned that the PaaS may have to be internally hosted at your workplace to ensure connectivity to internal databases.

## Python

Python 2.7 is the recommended minimum, although a 3.x release is advisable if unicode support is required. This package is tested to work with Python 2.7, 3.3, 3.4, and 3.5.

## MongoDB

MongoDB is required for persistent storage of runtime configurations, lookup tables, regex rules, and derivation rules. It also serves as an (optional, but recommended) home for record-level audit history. Also, since operational data will be stored here, you should have some sort of routine backup process in place.

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


## Scheduled Jobs

Scheduled jobs are likely the most robust option for consistent data cleaning.

# Examples

__Coming Soon: Red Hat's Marketing Operations implementation via Openshift__
