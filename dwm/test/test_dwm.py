import mongomock
from dwm import dwmAll
from dwm.test.test_lookup import lookup
#from .test_regex import regex
#from .test_derive import derive
from dwm.test.test_configs import configs
import dwm.test.test_records as test_records

## Initialize pre-test mongomock

db = mongomock.MongoClient().db

for row in lookup:

    db.lookup.insert(row)

for row in configs:

    db.config.insert(row)

## mongo collection config

mongoConfig = {
    "config": "config",
    "lookup": "lookup",
    "regex": "regex",
    "derive": "derive",
    "contactHistory": "contactHistory"
}

## Test against lookupAll

# genericValidation

def test_lookupAll_genericValidation_caught():

    # do stuff for testing
    dataOut = dwmAll(data = test_records.record_lookupAll_genericValidation_caught, mongoDb = db, mongoConfig=mongoConfig, configName='test_lookupAll_genericValidation')
    assert dataOut[0]['field1'] == ''

def test_lookupAll_genericValidation_uncaught():

    # do stuff for testing
    dataOut = dwmAll(data = test_records.record_lookupAll_genericValidation_uncaught, mongoDb = db, mongoConfig=mongoConfig, configName='test_lookupAll_genericValidation')
    assert dataOut[0]['field1'] != ''


## Teardown post-test mongomock
