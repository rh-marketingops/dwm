# Data structure definitions

## Input data

'''javascript
{
  "emailAddress": "testing@test.com",
  "field1": "Hi! I'm a field value"
}
'''

## Runtime settings

High-level settings dictating what actions DWM will run

 - Why not hard-code?
  - Allows for individual configuration of fields from a UI
  - Also allows one-time settings to be run (i.e., as a DWM Admin, I want to run validation and normalization only on the field "Job Role" for a specific segment)
  - Initial setup (before UI is built) will be akin to hard-coding

### Available fields

Field-level descriptions

'''javascript
{
  "fieldName": "jobRole",
  "fieldNameDisplay": "Job Role",
  "description": "Put a description of 'Job Role' here for the low, low price of $9.99! But wait, there's more!",
  "type": "picklist",
  "values": ["list", "of", "valid", "values"],
  "createdBy": "createdByUser",
  "createdDate": dateUnixtime,
  "lastModifiedBy": "modifiedByUser",
  "lastModifiedDate": dateUnixtime
},
{
  "fieldName": "firstName",
  "fieldNameDisplay": "First Name",
  "description": "Woah, it's a first name!",
  "type": "freeText",
  "createdBy": "createdByUser",
  "createdDate": dateUnixtime,
  "lastModifiedBy": "modifiedByUser",
  "lastModifiedDate": dateUnixtime
}
'''

### Run Config

Which fields are managed, and which cleaning functions are used

'''javascript
{
  "configName": "cron",
  "createdBy": "createdByUser",
  "createdDate": dateUnixtime,
  "lastModifiedBy": "modifiedByUser",
  "lastModifiedDate": dateUnixtime,
  "fields": {
    "field1": {
      "lookup": ["fieldSpecificLookup", "genericLookup", "normLookup", "fieldSpecificRegex", "genericRegex", "normRegex"],
      "fillGaps": {
        "netprospex": {
          "externalNameAPI": "Field_1"
        },
        "demandbase": {
          "externalNameAPI": "CField1"
        }
        },
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
  }
}
'''

#### Setting types

- validation:
  - fieldSpecificLookup: lookup exact value for field-specific bad data
  - fieldSpecificRegex: use field-specific regex for bad data
  - genericLookup: lookup exact value for generic bad data
  - genericRegex: use generic regex for bad data
- fillGaps
  - netprospex
  - demandbase
- deriveValue
  - dict key: int value for priority order
  - type:
  - fieldSet: list of field names on which to lookup
  - overwrite: lookup value even if field already has value
- normalization
  - normLookup: lookup exact value for field-specific normalization
  - normRegex: use field-specific regex for normalization

### Ad-hoc function config

To insert user-defined functions into the standard DWM process. One example is US zipcode cleanup.

'''javascript
{
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
    "1": "okayjustonemore"
    "2": "ireallymeanitthistime"
  },
  "beforeDeriveData": {
    "1": "imtired"
  },
  "afterProcessing": {
    "1": "iwantaburrito"
  }
}
'''

### Field Mappings

Maps the fields defined above to existing fields in external systems (i.e., Eloqua, Redshift) for export/import

'''javascript
{
  "externalSystemName": "eloqua_prod"
  "externalFieldName": "C_Job_Role11",
  "fieldName": "jobRole"
}
'''

## Data Cleaning "Rules"

### Data lookup

Defines a lookup value for transforming a single field value (generic or field-specific validation, normalization)

'''javascript
//generic validation lookup
{
  "type": "genericLookup",
  "find": "aaaaaaaaaaaa"
}

//field-specific validation lookup
{
  "type": "fieldSpecificLookup",
  "fieldName": "field1",
  "find": "thisemailshouldnotbehere@wtf.org"
}

// normalization lookup
{
  "type": "normLookup",
  "fieldName": "field1",
  "find": "i'm kind of the right value",
  "replace": "i'm the right value"
}
'''

### Data derivation

Defines a potentially multi-field based lookup mapped to a single field (fill-gaps or derived fields; i.e. Persona is a combination of Job Role and Department).
Keeping the ```lookupVals``` in a sub-document allows for indexing on the ```derive``` collection.

'''javascript
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
    "jobRole": "Manager",
    "department": "IT - Applications"
  },
  "value": "IT Decision Maker"
}
'''

### Regex

Defines a regular expression transformation that will be applied to a single field value (generic or field-specific validation, normalization).
Should have a "description" to let others know what the regex is supposed to do.

'''javascript
// generic validation regex
{
  "type": "genericRegex",
  "pattern": "[coolpattern]",
  "description": "looks for strings that are all the same character"
}

// field-specific validation regex
{
  "type": "fieldSpecificRegex",
  "fieldName": "field1",
  "pattern": "[anothercoolpattern]",
  "description": "looks for string of only numbers"
}

// normalization regex
{
  "type": "normRegex",
  "fieldName": "field1",
  "pattern": "[yesanother]",
  "replace": "Programmer/Developer",
  "description": "looks for 'developer' job roles"
}

// derive value by regex on another field
{
  "type": "deriveRegex",
  "fieldName": "field1",
  "deriveFieldName": "field2",
  "pattern": "^coolpattern$",
  "replace": "Programmer/Developer",
  "description": "looks for 'developer' job titles to derive job role"
}
'''

### Indexing

To optimize performance (specifically for data derive lookups), the following indexes should be implemented within MongoDB:

'''javascript

// 'lookup' collection
db.lookup.ensureIndex({'type': 1, 'find': 1})
db.lookup.ensureIndex({'type': 1, 'fieldName': 1, 'find': 1})

// 'derive' collection
db.derive.ensureIndex({'type': 1, "fieldName": 1, "lookupVals": 1})

'''

## Audit

### Contact history
Captures contact-level field changes

'''javascript
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
'''
