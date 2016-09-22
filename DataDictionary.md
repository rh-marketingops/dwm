# DWM - Data Dictionary

## Input data

Data input is expected to be one dictionary per record to be cleaned. Keys map to field names.

If ```writeContactHistory``` is configured, then at a minimum that field must be included in the dictionary for each record.

```python
{
  "emailAddress": "testing@test.com",
  "field1": "Hi! I'm a field value"
}
```

## Stored Settings

Stored settings are documents stored in the production MongoDB that dictate how DWM operates. This includes the actual cleaning rules/values which will be applied, configuration for what rules to apply to which fields, record-level histories, and field information which can be displayed in a UI to help business users better define their configurations.

The following defines each collection.

### Available fields

Field-level descriptions. Currently not used in processing, but defining schema now as future versions may include validation of field values based on field constraints.

```javascript
{
  "fieldName": "jobRole",
  "fieldNameDisplay": "Job Role",
  "description": "Put a description of 'Job Role' here for the low, low price of $9.99! But wait, there's more!",
  "type": "picklist",
  "values": ["list", "of", "valid", "values"],
  "createdBy": "createdByUser",
  "createdDate": dateUnixtime,
  "lastModifiedBy": "modifiedByUser",
  "lastModifiedDate": dateUnixtime,
  "fieldSources": {
    "eloquaProd": "eloquaFieldName",
    "databaseDev": "databaseFieldName"
  }
},
{
  "fieldName": "firstName",
  "fieldNameDisplay": "First Name",
  "description": "Woah, it's a first name!",
  "type": "freeText",
  "createdBy": "createdByUser",
  "createdDate": dateUnixtime,
  "lastModifiedBy": "modifiedByUser",
  "lastModifiedDate": dateUnixtime,
  "fieldSources": {
    "eloquaProd": "eloquaFieldName",
    "databaseDev": "databaseFieldName"
  }
}
```

### config

Which fields are cleaned by a single run.

To be cleaned, a field must be present in the config document *and* in the data record passed to DWM:
- If the config includes ```jobRole``` and the record passed to DWM includes the field ```jobRole```, then cleaning rules will be applied to ```jobRole```
- If the config includes ```jobRole``` but the record passed to DWM does *not* include ```jobRole```, then cleaning rules will not be applied to ```jobRole```
- if the config does *not* include ```jobRole``` but the record passed to DWM *does* include ```jobRole```, then cleaning rules will not be applied to ```jobRole```

#### Why store config separately from code?

- Flexibility
  - Ability to run multiple different configurations for different circumstances
    - A standard configuration runs on a cron job every hour
    - A single user decides to run a one-time cleanup of a field
    - Standard configuration separate from cron job provided for API users
  - Allow creation of UI for business users to easily modify configuration
- Transparency + Security
 - Allow non-owner business users to view the current configuration; promotes openness of data cleaning practices

#### Special cases for ```derive``` configurations

Similarly, for ```deriveValue```, ```deriveRegex```, ```deriveIncludes```, and ```copyValue```, derivation rules will only be applied when the specified field *and all* of the fields listed in ```fieldSet``` are present in the record passed to DWM:
- If the config includes a ```deriveValue``` rule for ```persona``` which requires ```jobRole``` and ```department```, and the record passed includes all three, then DWM will attempt to derive ```persona```
- If the config includes a ```deriveValue``` rule for ```persona``` which requires ```jobRole``` and ```department```, and the record passed only includes ```jobRole``` and ```persona```, then it will not attempt to derive a value for ```persona```

Also included are two parameters:

- overwrite: if the target field already has a value, should it be overwritten?
- blankIfNoMatch: if the derive rules do not find a match, should the field be cleared out?

If the order of derivation is important in your use case, then order the fields accordingly in the JSON doc. Then, when establishing a connection to MongoDB:

```python
from collections import OrderedDict
client = pymongo.MongoClient('connectURL', document_class=OrderedDict)
```

#### Example:

```javascript
{
  "configName": "configyMcConfigFace",
  "createdBy": "createdByUser",
  "createdDate": dateUnixtime,
  "lastModifiedBy": "modifiedByUser",
  "lastModifiedDate": dateUnixtime,
  "fields": {
    "field1": {
      "lookup": ["fieldSpecificLookup", "genericLookup", "normLookup", "fieldSpecificRegex", "genericRegex", "normRegex", "normIncludes"],
      "derive": {
        "1": {
          "type": "deriveValue",
          "fieldSet": ["field2", "field3"],
          "overwrite": true,
          "blankIfNoMatch": false
          },
        "2": {
          "type": "copyValue",
          "fieldSet": ["field3"],
          "overwrite": false
          },
        "4": {
          "type": "deriveRegex",
          "fieldSet": ["field6"],
          "overwrite": true,
          "blankIfNoMatch": false
        },
        "3": {
          "type": "deriveValue",
          "fieldSet": ["field2", "field4"],
          "overwrite": true,
          "blankIfNoMatch": true
        },
        "5": {
          "type": "deriveIncludes",
          "fieldSet": ["field5"],
          "overwrite": true,
          "blankIfNoMatch": false
        }
      }
    },
    ...
  },
  "userDefinedFunctions": {
    "beforeGenericValidation": {
      "1": "somefunction",
      "2": "anotherfunction"
    },
    "beforeGenericRegex": {
      "1": "heylookafunction"
    },
    "beforeFieldSpecificValidation": {
      "1": "reallyanotherone"
    },
    "beforeFieldSpecificRegex": {
      "1": "okaythisisgettingridiculous"
    },
    "beforeNormalization": {
      "1": "igiveup"
    },
    "beforeNormalizationRegex": {
      "1": "okayjustonemore",
      "2": "ireallymeanitthistime"
    },
    "beforeNormalizationIncludes": {
      "1": "okayanother"
    },
    "beforeDeriveData": {
      "1": "imtired"
    },
    "afterProcessing": {
      "1": "iwantaburrito"
    }
  },
  "history": {
    "writeContactHistory": true,
    "returnHistoryId": true,
    "returnHistoryField": "historyId",
    "histIdField": {"name": "emailAddress", "value": "emailAddress"}
  }
}
```

### genericLookup

```javascript
//generic validation lookup
{
  "type": "genericLookup",
  "find": "aaaaaaaaaaaa"
}
```

### fieldSpecificLookup

```javascript

//field-specific validation lookup
{
  "type": "fieldSpecificLookup",
  "fieldName": "field1",
  "find": "thisemailshouldnotbehere@wtf.org"
}
```

### normLookup

```javascript

// normalization lookup
{
  "type": "normLookup",
  "fieldName": "field1",
  "find": "i'm kind of the right value",
  "replace": "i'm the right value"
}
```

### normIncludes

```javascript

// normalization includes
{
  "fieldName": "field1",
  "includes": "val,stuff,things",
  "excludes": "others,not",
  "begins": "startval",
  "ends": "endval",
  "replace": "goodvalue"
}
```

### deriveValue

Defines a potentially multi-field based lookup mapped to a single field (fill-gaps or derived fields; i.e. Persona is a combination of Job Role and Department).
Keeping the ```lookupVals``` in a sub-document allows for indexing on the ```derive``` collection.

*IMPORTANT* ```lookupVals``` sub-document must be keyed alphabetically! This allows both indexing and querying to work properly.

```javascript
// single-value derived lookup
{
  "type": "deriveValue",
  "fieldName": "superRegion",
  "lookupVals": {
    "country": "US"
  },
  "value": "NA"
}

// multi-value derived lookup
{
  "type": "deriveValue",
  "fieldName": "persona",
  "lookupVals": {
    "jobRole": "MANAGER",
    "department": "IT - APPLICATIONS"
  },
  "value": "IT Decision Maker"
}
```

### deriveIncludes

```javascript

// derive includes
{
  "fieldName": "field1",
  "deriveFieldName": "field2"
  "includes": "val,stuff,things",
  "excludes": "others,not",
  "begins": "startval",
  "ends": "endval",
  "replace": "goodvalue"
}
```

### normIncludes

```javascript

// normalization includes
{
  "fieldName": "field1",
  "deriveFieldName": "field2",
  "includes": "val,stuff,things",
  "excludes": "others,not",
  "begins": "startval",
  "ends": "endval"
}
```

### deriveRegex

```javascript

// derive value by regex on another field
{
  "type": "deriveRegex",
  "fieldName": "field1",
  "deriveFieldName": "field2",
  "pattern": "^coolpattern$",
  "replace": "Programmer/Developer",
  "description": "looks for 'developer' job titles to derive job role"
}
```

### genericRegex

```javascript
// generic validation regex
{
  "type": "genericRegex",
  "pattern": "[coolpattern]",
  "description": "looks for strings that are all the same character"
}
```

### fieldSpecificRegex

```javascript

// field-specific validation regex
{
  "type": "fieldSpecificRegex",
  "fieldName": "field1",
  "pattern": "[anothercoolpattern]",
  "description": "looks for string of only numbers"
}
```

### normRegex

```javascript

// normalization regex
{
  "type": "normRegex",
  "fieldName": "field1",
  "pattern": "[yesanother]",
  "replace": "Programmer/Developer",
  "description": "looks for 'developer' job roles"
}
```

### contactHistory

Provides an audit history of records to promote transparency and allow for troubleshooting.

```javascript
{
  "emailAddress": "pmccrevice@jyang.org",
  "configName": "cron",
  "runTime": runUnixtime,
  "fields": {
    "field1":{
      "fieldSpecificLookup": {
        "from": "aaaaaaaaaaaa",
        "to": ""
      },
      "fieldSpecificRegex": {
        "from": "aaaaaaaaaaaa",
        "to": "",
        "pattern": "someRegexPattern"
      }
      "deriveValue": {
        "from": "",
        "to": "this is cool!",
        "using": {
          "field2": "field2Value",
          "field3": "field3Value"
        }
      }
    }
  }
}
```

## Indexing

To optimize performance (specifically for deriveValue lookups), the following indexes should be implemented within MongoDB:

```javascript

db.genericLookup.ensureIndex({"find": 1})
db.fieldSpecificLookup.ensureIndex({"fieldName": 1, "find": 1})
db.normLookup.ensureIndex({"fieldName": 1, "find": 1})
db.normIncludes.ensureIndex({"fieldName": 1})

db.fieldSpecificRegex.ensureIndex({"fieldName": 1})
db.normRegex.ensureIndex({"fieldName": 1})

db.deriveValue.ensureIndex({"fieldName": 1, "lookupVals": 1})
db.deriveRegex.ensureIndex({"fieldName": 1})
db.deriveIncludes.ensureIndex({"fieldName": 1})

```
