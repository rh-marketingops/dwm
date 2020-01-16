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
- `normIncludes`: replace 'almost' values based on at least one of the following: includes strings, excludes strings, starts with string, ends with string

## Derivation

Derivation is the management of fields designed to help business users more easily make decisions, but are not explicitly collected. One example is a "Super Region" field. Although "Country" is a value that is likely collected, users of the database may only need to filter to a general region to do their jobs.

DWM uses three types of derivation:

- `deriveValue`: given input values from one or more fields, find the corresponding output value; i.e., for `jobRole='Manager'` and `department='IT'`, then set `persona='IT Decision Maker'`
- `copyValue`: given an input value from one field, copy that value to the target field
- `deriveRegex`: given an input value from one field, derive target field value using regular expressions
- `deriveIncludes`: given an input value from one field, derive target field based on at least one of the following: includes strings, excludes strings, starts with string, ends with string

Within the runtime configuration, derivation rules are ordered within a dictionary to maintain rule-hierarchy. So, if Rule 1 does not yield a result, then Rule 2 would be tried. The process will exit after one of the derivation rules produces a new value.

## User-Defined Functions

The above three processes are the most common processes that need to be applied to data, but not everything can be planned for. User-Defined functionality is designed to fill this gap. For instance, US Zipcodes can have some fairly basic and consistent transformations applied to make the data easier to work with (i.e., strip off trailing hypen/number combos, left pad with 0s in case of bad spreadsheet formatting), but those rules don't fall into any of the above categories.

Also included may be third-party data enrichment. For example, if you have an API contract with a company that provides IP address geolocation, or provides additional company info based on email domain, you can define a function to interact with that API and pull additional data into the fields of interest.

## Order

We've found this to be the most efficient order in which to run the above cleaning types.

1. Generic Validation
2. Field-specific Validation
3. Normalization
4. Derive Data (aka "Fill-in-the-gaps", depending on field type)

## Audit History

Record-level audit history is a record of what changes were made to which data fields. This includes what the previous value was, what the new/replacement value was, and what rule caused the change. The record is somewhat akin to a git commit, in that it only records where changes were made, and does not keep a record of anything that remained unchanged. Although it is optional in this package, it is recommended for any automation of these processes to provide both a record for troubleshooting and transparency for the business users of the database.

# Usage

```python
from pymongo import MongoClient
from dwm import DWM

# Initialize mongo connection where rules are stored
my_mongo = MongoClient()

field_config = {
  'field1': {
    'lookup': ['genericLookup', 'genericRegex', 'fieldSpecificLookup',
               'fieldSpecificRegex', 'normLookup', 'normRegex', 'normIncludes'],
    'derive': [
      {
        'type': 'deriveIncludes',
        'fieldSet': ['field2'],
        'options': ['overwrite', 'blankIfNoMatch']
      }
    ]
  }
}

# Initialize DWM instance
dwm_instance = (
  name='MyDWM',
  mongo=my_mongo,
  fields=field_config
)

# Create a test record to run through DWM
test_record = {
  'field1': 'potentiallybaddata',
  'field2': 'potentialderivematch'
}

# Run through DWM and return cleaned record = history/changes
clean_record, hist = dwm_instance.run(test_record)

```

## Lookups, Derivation, and Regex rules

A complete schema for these items is in the DataDictionary.md file. Also included is a recommendation for indexes to improve performance.

## User-Defined Functions

User-Defined functions must take exactly two inputs, `data` (a single dictionary of data to which transformations are applied) and `histObj` (a dictionary object used to record field-level changes), and output the same two (with changes applied to `data` and any relevant updates made to `histObj`). Helper functions for recording history are included in the dwm package.

UDFs should ideally be defined in a file separate from the script calling the DWM functions, then loaded in independently.

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
from dwm import Dwm
from udf import myFunction

# Set up UDF config to pass to Dwm
udf_config = {
  'beforeDerive': [myFunction]
}

# Initialize DWM instance
dwm_instance = (
  name='MyDWM',
  mongo=my_mongo,
  udfs=udf_config
)

```
