import mongomock
from dwm import dwmAll
from dwm.test.test_lookup import lookup
from .test_regex import regex
from .test_derive import derive
from dwm.test.test_configs import configs
import dwm.test.test_records as test_records

## Initialize pre-test mongomock

db = mongomock.MongoClient().db

for row in lookup:

    db.lookup.insert_one(row)

for row in regex:

    db.regex.insert_one(row)

for row in derive:

    db.derive.insert_one(row)

for row in configs:

    db.config.insert_one(row)

## mongo collection config

mongoConfig = {
    "config": "config",
    "lookup": "lookup",
    "regex": "regex",
    "derive": "derive",
    "contactHistory": "contactHistory"
}

## Test against lookupAll

# genericLookup

def test_lookupAll_genericLookup_caught():

    dataOut = dwmAll(data = test_records.record_lookupAll_genericLookup_caught, mongoDb = db, mongoConfig=mongoConfig, configName='test_lookupAll_genericLookup')
    assert dataOut[0]['field1'] == ''

def test_lookupAll_genericLookup_uncaught():

    dataOut = dwmAll(data = test_records.record_lookupAll_genericLookup_uncaught, mongoDb = db, mongoConfig=mongoConfig, configName='test_lookupAll_genericLookup')
    assert dataOut[0]['field1'] != ''

def test_lookupAll_genericLookup_notChecked():

    dataOut = dwmAll(data = test_records.record_lookupAll_genericLookup_notChecked, mongoDb = db, mongoConfig=mongoConfig, configName='test_lookupAll_genericLookup')
    assert dataOut[0]['field2'] != ''

# fieldSpecificLookup

def test_lookupAll_fieldSpecificLookup_caught():

    dataOut = dwmAll(data = test_records.record_lookupAll_fieldSpecificLookup_caught, mongoDb = db, mongoConfig=mongoConfig, configName='test_lookupAll_fieldSpecificLookup')
    assert dataOut[0]['field1'] == ''

def test_lookupAll_fieldSpecificLookup_uncaught():

    dataOut = dwmAll(data = test_records.record_lookupAll_fieldSpecificLookup_uncaught, mongoDb = db, mongoConfig=mongoConfig, configName='test_lookupAll_fieldSpecificLookup')
    assert dataOut[0]['field1'] != ''

def test_lookupAll_fieldSpecificLookup_notChecked():

    dataOut = dwmAll(data = test_records.record_lookupAll_fieldSpecificLookup_notChecked, mongoDb = db, mongoConfig=mongoConfig, configName='test_lookupAll_fieldSpecificLookup')
    assert dataOut[0]['field2'] != ''

# normLookup

def test_lookupAll_normLookup_caught():

    # do stuff for testing
    dataOut = dwmAll(data = test_records.record_lookupAll_normLookup_caught, mongoDb = db, mongoConfig=mongoConfig, configName='test_lookupAll_normLookup')
    assert dataOut[0]['field1'] == 'goodvalue'

def test_lookupAll_normLookup_uncaught():

    dataOut = dwmAll(data = test_records.record_lookupAll_normLookup_uncaught, mongoDb = db, mongoConfig=mongoConfig, configName='test_lookupAll_normLookup')
    assert dataOut[0]['field1'] != 'goodvalue'

def test_lookupAll_normLookup_notChecked():

    dataOut = dwmAll(data = test_records.record_lookupAll_normLookup_notChecked, mongoDb = db, mongoConfig=mongoConfig, configName='test_lookupAll_normLookup')
    assert dataOut[0]['field2'] != 'goodvalue'

# genericRegex

def test_regexAll_genericRegex_caught():

    dataOut = dwmAll(data = test_records.record_regexAll_genericRegex_caught, mongoDb = db, mongoConfig=mongoConfig, configName='test_regexAll_genericRegex')
    assert dataOut[0]['field1'] == ''

def test_regexAll_genericRegex_uncaught():

    dataOut = dwmAll(data = test_records.record_regexAll_genericRegex_uncaught, mongoDb = db, mongoConfig=mongoConfig, configName='test_regexAll_genericRegex')
    assert dataOut[0]['field1'] != ''

def test_regexAll_genericRegex_notChecked():

    dataOut = dwmAll(data = test_records.record_regexAll_genericRegex_notChecked, mongoDb = db, mongoConfig=mongoConfig, configName='test_regexAll_genericRegex')
    assert dataOut[0]['field2'] != ''

# fieldSpecificRegex

def test_regexAll_fieldSpecificRegex_caught():

    dataOut = dwmAll(data = test_records.record_regexAll_fieldSpecificRegex_caught, mongoDb = db, mongoConfig=mongoConfig, configName='test_regexAll_fieldSpecificRegex')
    assert dataOut[0]['field1'] == ''

def test_regexAll_fieldSpecificRegex_uncaught():

    dataOut = dwmAll(data = test_records.record_regexAll_fieldSpecificRegex_uncaught, mongoDb = db, mongoConfig=mongoConfig, configName='test_regexAll_fieldSpecificRegex')
    assert dataOut[0]['field1'] != ''

def test_regexAll_fieldSpecificRegex_notChecked():

    dataOut = dwmAll(data = test_records.record_regexAll_fieldSpecificRegex_notChecked, mongoDb = db, mongoConfig=mongoConfig, configName='test_regexAll_fieldSpecificRegex')
    assert dataOut[0]['field2'] != ''

# normRegex

def test_regexAll_normRegex_caught():

    dataOut = dwmAll(data = test_records.record_regexAll_normRegex_caught, mongoDb = db, mongoConfig=mongoConfig, configName='test_regexAll_normRegex')
    assert dataOut[0]['field1'] == 'goodvalue'

def test_regexAll_normRegex_uncaught():

    # do stuff for testing
    dataOut = dwmAll(data = test_records.record_regexAll_normRegex_uncaught, mongoDb = db, mongoConfig=mongoConfig, configName='test_regexAll_normRegex')
    assert dataOut[0]['field1'] != 'goodvalue'

def test_regexAll_normRegex_notChecked():

    dataOut = dwmAll(data = test_records.record_regexAll_normRegex_notChecked, mongoDb = db, mongoConfig=mongoConfig, configName='test_regexAll_normRegex')
    assert dataOut[0]['field2'] != 'goodvalue'

# deriveValue

def test_deriveAll_deriveValue_caught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveValue_caught, mongoDb = db, mongoConfig=mongoConfig, configName='test_deriveAll_deriveValue')
    assert dataOut[0]['field1'] == 'newvalue'

def test_deriveAll_deriveValue_uncaught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveValue_uncaught, mongoDb = db, mongoConfig=mongoConfig, configName='test_deriveAll_deriveValue')
    assert dataOut[0]['field1'] != 'newvalue'

def test_deriveAll_deriveValue_notChecked():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveValue_notChecked, mongoDb = db, mongoConfig=mongoConfig, configName='test_deriveAll_deriveValue')
    assert dataOut[0]['field3'] == ''

def test_deriveAll_deriveValue_overwriteFalse():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveValue_overwriteFalse, mongoDb = db, mongoConfig=mongoConfig, configName='test_deriveAll_deriveValue_overwriteFalse')
    assert dataOut[0]['field1'] == 'oldvalue'


# copyValue

def test_deriveAll_copyValue():

    dataOut = dwmAll(data = test_records.record_deriveAll_copyValue, mongoDb = db, mongoConfig=mongoConfig, configName='test_deriveAll_copyValue')
    assert dataOut[0]['field1'] == 'newvalue'

# deriveRegex

def test_deriveAll_deriveRegex_caught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveRegex_caught, mongoDb = db, mongoConfig=mongoConfig, configName='test_deriveAll_deriveRegex')
    assert dataOut[0]['field1'] == 'newvalue'

def test_deriveAll_deriveRegex_uncaught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveRegex_uncaught, mongoDb = db, mongoConfig=mongoConfig, configName='test_deriveAll_deriveRegex')
    assert dataOut[0]['field1'] != 'newvalue'

def test_deriveAll_deriveRegex_notChecked():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveRegex_notChecked, mongoDb = db, mongoConfig=mongoConfig, configName='test_deriveAll_deriveRegex')
    assert dataOut[0]['field3'] == ''
