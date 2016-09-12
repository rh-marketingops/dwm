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

#### Special cases for ```derive``` configurations

Similarly, for ```deriveValue```, ```deriveRegex```, and ```copyValue```, derivation rules will only be applied when the specified field *and all* of the fields listed in ```fieldSet``` are present in the record passed to DWM:
- If the config includes a ```deriveValue``` rule for ```persona``` which requires ```jobRole``` and ```department```, and the record passed includes all three, then DWM will attempt to derive ```persona```
- If the config includes a ```deriveValue``` rule for ```persona``` which requires ```jobRole``` and ```department```, and the record passed only includes ```jobRole``` and ```persona```, then it will not attempt to derive a value for ```persona```

Also included are two parameters:

- overwrite: if the target field already has a value, should it be overwritten?
- blankIfNoMatch: if the derive rules do not find a match, should the field be cleared out? 

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
      "lookup": ["fieldSpecificLookup", "genericLookup", "normLookup", "fieldSpecificRegex", "genericRegex", "normRegex"],
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


## Runtime settings

High-level settings dictating what actions DWM will run

 - Why not hard-code?
  - Allows for individual configuration of fields from a UI
  - Also allows one-time settings to be run (i.e., as a DWM Admin, I want to run validation and normalization only on the field "Job Role" for a specific segment)
  - Initial setup (before UI is built) will be akin to hard-coding



### Run Config

Which fields are managed, and which cleaning functions are used

```javascript
{
  "configName": "cron",
  "createdBy": "createdByUser",
  "createdDate": dateUnixtime,
  "lastModifiedBy": "modifiedByUser",
  "lastModifiedDate": dateUnixtime,
  "fields": {
    "field1": {
      "lookup": ["fieldSpecificLookup", "genericLookup", "normLookup", "fieldSpecificRegex", "genericRegex", "normRegex"],
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
          "overwrite": false,
          "blankIfNoMatch": false
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

#### Setting types

- validation:
  - fieldSpecificLookup: lookup exact value for field-specific bad data
  - fieldSpecificRegex: use field-specific regex for bad data
  - genericLookup: lookup exact value for generic bad data
  - genericRegex: use generic regex for bad data
- deriveValue
  - dict key: int value for priority order
  - type:
  - fieldSet: list of field names on which to lookup
  - overwrite: lookup value even if field already has value
- normalization
  - normLookup: lookup exact value for field-specific normalization
  - normRegex: use field-specific regex for normalization
- userDefinedFunctions
  - beforeGenericValidation
  - beforeGenericRegex
  - beforeFieldSpecificValidation
  - beforeFieldSpecificRegex
  - beforeNormalization
  - beforeNormalizationRegex
  - beforeDeriveData
  - afterProcessing
- history
  - writeContactHistory: Should a history record be written to the database
  - returnHistoryId: return MongoDB ```_id``` of history record
  - returnHistoryField: if returnHistoryId, field name of returned ```_id```
  - histIdField: Identifier for history records

## Data cleaning schema

The following "schema" are grouped by which collection dwm expects to find them in.

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

### Indexing

To optimize performance (specifically for deriveValue lookups), the following indexes should be implemented within MongoDB:

```javascript

db.genericLookup.ensureIndex({"find": 1})
db.fieldSpecificLookup.ensureIndex({"fieldName": 1, "find": 1})
db.normLookup.ensureIndex({"fieldName": 1, "find": 1})

db.fieldSpecificRegex.ensureIndex({"fieldName": 1})
db.normRegex.ensureIndex({"fieldName": 1})

db.deriveValue.ensureIndex({"fieldName": 1, "lookupVals": 1})
db.deriveRegex.ensureIndex({"fieldName": 1})

```

## Audit

### Contact history
Captures contact-level field changes

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
