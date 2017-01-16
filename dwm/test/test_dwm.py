import mongomock
from nose.tools import *
from mock import patch
from dwm import dwmAll

from .test_genericLookup import genericLookup
from .test_fieldSpecificLookup import fieldSpecificLookup
from .test_normLookup import normLookup

from .test_genericRegex import genericRegex
from .test_fieldSpecificRegex import fieldSpecificRegex
from .test_normRegex import normRegex

from .test_normIncludes import normIncludes
from .test_deriveIncludes import deriveIncludes

from .test_deriveValue import deriveValue
from .test_deriveRegex import deriveRegex

from dwm.test.test_configs import configs
import dwm.test.test_records as test_records
import dwm.test.test_udf as test_udf
from dwm.test.test_udf import ex_udf, sort_udf_1, sort_udf_2
import dwm.cleaning as cleaning
import dwm.helpers as helpers

## Initialize pre-test mongomock

db = mongomock.MongoClient().db

for row in genericLookup:

    db.genericLookup.insert_one(row)

for row in fieldSpecificLookup:

    db.fieldSpecificLookup.insert_one(row)

for row in normLookup:

    db.normLookup.insert_one(row)

for row in genericRegex:

    db.genericRegex.insert_one(row)

for row in fieldSpecificRegex:

    db.fieldSpecificRegex.insert_one(row)

for row in normRegex:

    db.normRegex.insert_one(row)

for row in normIncludes:

    db.normIncludes.insert_one(row)

for row in deriveValue:

    db.deriveValue.insert_one(row)

for row in deriveRegex:

    db.deriveRegex.insert_one(row)

for row in deriveIncludes:

    db.deriveIncludes.insert_one(row)

for row in configs:

    db.config.insert_one(row)

######################################
## Test lookups

# Test verbosity

def test_verbose():

    dataOut = dwmAll(data = test_records.record_lookupAll_genericLookup_caught, db = db, configName='test_lookupAll_genericLookup', verbose=True)
    assert dataOut[0]['field1'] == ''

# genericLookup

def test_lookupAll_genericLookup_caught():

    dataOut = dwmAll(data = test_records.record_lookupAll_genericLookup_caught, db = db, configName='test_lookupAll_genericLookup')
    assert dataOut[0]['field1'] == ''

def test_lookupAll_genericLookup_uncaught():

    dataOut = dwmAll(data = test_records.record_lookupAll_genericLookup_uncaught, db = db, configName='test_lookupAll_genericLookup')
    assert dataOut[0]['field1'] != ''

def test_lookupAll_genericLookup_notChecked():

    dataOut = dwmAll(data = test_records.record_lookupAll_genericLookup_notChecked, db = db, configName='test_lookupAll_genericLookup')
    assert dataOut[0]['field2'] != ''

# fieldSpecificLookup

def test_lookupAll_fieldSpecificLookup_caught():

    dataOut = dwmAll(data = test_records.record_lookupAll_fieldSpecificLookup_caught, db = db, configName='test_lookupAll_fieldSpecificLookup')
    assert dataOut[0]['field1'] == ''

def test_lookupAll_fieldSpecificLookup_uncaught():

    dataOut = dwmAll(data = test_records.record_lookupAll_fieldSpecificLookup_uncaught, db = db, configName='test_lookupAll_fieldSpecificLookup')
    assert dataOut[0]['field1'] != ''

def test_lookupAll_fieldSpecificLookup_notChecked():

    dataOut = dwmAll(data = test_records.record_lookupAll_fieldSpecificLookup_notChecked, db = db, configName='test_lookupAll_fieldSpecificLookup')
    assert dataOut[0]['field2'] != ''

# normLookup

def test_lookupAll_normLookup_caught():

    # do stuff for testing
    dataOut = dwmAll(data = test_records.record_lookupAll_normLookup_caught, db = db, configName='test_lookupAll_normLookup')
    assert dataOut[0]['field1'] == 'goodvalue'

def test_lookupAll_normLookup_uncaught():

    dataOut = dwmAll(data = test_records.record_lookupAll_normLookup_uncaught, db = db, configName='test_lookupAll_normLookup')
    assert dataOut[0]['field1'] != 'goodvalue'

def test_lookupAll_normLookup_notChecked():

    dataOut = dwmAll(data = test_records.record_lookupAll_normLookup_notChecked, db = db, configName='test_lookupAll_normLookup')
    assert dataOut[0]['field2'] != 'goodvalue'

##############################
## Test regex
# genericRegex

def test_regexAll_genericRegex_caught():

    dataOut = dwmAll(data = test_records.record_regexAll_genericRegex_caught, db = db, configName='test_regexAll_genericRegex')
    assert dataOut[0]['field1'] == ''

def test_regexAll_genericRegex_uncaught():

    dataOut = dwmAll(data = test_records.record_regexAll_genericRegex_uncaught, db = db, configName='test_regexAll_genericRegex')
    assert dataOut[0]['field1'] != ''

def test_regexAll_genericRegex_notChecked():

    dataOut = dwmAll(data = test_records.record_regexAll_genericRegex_notChecked, db = db, configName='test_regexAll_genericRegex')
    assert dataOut[0]['field2'] != ''

# fieldSpecificRegex

def test_regexAll_fieldSpecificRegex_caught():

    dataOut = dwmAll(data = test_records.record_regexAll_fieldSpecificRegex_caught, db = db, configName='test_regexAll_fieldSpecificRegex')
    assert dataOut[0]['field1'] == ''

def test_regexAll_fieldSpecificRegex_uncaught():

    dataOut = dwmAll(data = test_records.record_regexAll_fieldSpecificRegex_uncaught, db = db, configName='test_regexAll_fieldSpecificRegex')
    assert dataOut[0]['field1'] != ''

def test_regexAll_fieldSpecificRegex_notChecked():

    dataOut = dwmAll(data = test_records.record_regexAll_fieldSpecificRegex_notChecked, db = db, configName='test_regexAll_fieldSpecificRegex')
    assert dataOut[0]['field2'] != ''

# normRegex

def test_regexAll_normRegex_caught():

    dataOut = dwmAll(data = test_records.record_regexAll_normRegex_caught, db = db, configName='test_regexAll_normRegex')
    assert dataOut[0]['field1'] == 'goodvalue'

def test_regexAll_normRegex_uncaught():

    # do stuff for testing
    dataOut = dwmAll(data = test_records.record_regexAll_normRegex_uncaught, db = db, configName='test_regexAll_normRegex')
    assert dataOut[0]['field1'] != 'goodvalue'

def test_regexAll_normRegex_notChecked():

    dataOut = dwmAll(data = test_records.record_regexAll_normRegex_notChecked, db = db, configName='test_regexAll_normRegex')
    assert dataOut[0]['field2'] != 'goodvalue'

# normIncludes

def test_normIncludes_included_caught():

    dataOut = dwmAll(data = test_records.record_normIncludes_included_caught, db = db, configName='test_normIncludes')
    assert dataOut[0]['field1'] == 'goodvalue'

def test_normIncludes_included_uncaught():

    dataOut = dwmAll(data = test_records.record_normIncludes_included_uncaught, db = db, configName='test_normIncludes')
    assert dataOut[0]['field1'] != 'goodvalue'

def test_normIncludes_excluded_caught():

    dataOut = dwmAll(data = test_records.record_normIncludes_excluded_caught, db = db, configName='test_normIncludes')
    assert dataOut[0]['field1'] != 'goodvalue'

def test_normIncludes_excluded_uncaught():

    dataOut = dwmAll(data = test_records.record_normIncludes_excluded_uncaught, db = db, configName='test_normIncludes')
    assert dataOut[0]['field1'] == 'goodvalue'

def test_normIncludes_begins_caught():

    dataOut = dwmAll(data = test_records.record_normIncludes_begins_caught, db = db, configName='test_normIncludes')
    assert dataOut[0]['field1'] == 'goodvalue'

def test_normIncludes_begins_uncaught():

    dataOut = dwmAll(data = test_records.record_normIncludes_begins_uncaught, db = db, configName='test_normIncludes')
    assert dataOut[0]['field1'] != 'goodvalue'

def test_normIncludes_ends_caught():

    dataOut = dwmAll(data = test_records.record_normIncludes_ends_caught, db = db, configName='test_normIncludes')
    assert dataOut[0]['field1'] == 'goodvalue'

def test_normIncludes_ends_uncaught():

    dataOut = dwmAll(data = test_records.record_normIncludes_ends_uncaught, db = db, configName='test_normIncludes')
    assert dataOut[0]['field1'] != 'goodvalue'

def test_normIncludes_notChecked():

    dataOut = dwmAll(data = test_records.record_normIncludes_notChecked, db = db, configName='test_normIncludes')
    assert dataOut[0]['field2'] != 'goodvalue'


###################################
## Test derive
# deriveValue

def test_deriveAll_deriveValue_caught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveValue_caught, db = db, configName='test_deriveAll_deriveValue')
    assert dataOut[0]['field1'] == 'newvalue'

def test_deriveAll_deriveValue_uncaught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveValue_uncaught, db = db, configName='test_deriveAll_deriveValue')
    assert dataOut[0]['field1'] != 'newvalue'

def test_deriveAll_deriveValue_notChecked():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveValue_notChecked, db = db, configName='test_deriveAll_deriveValue')
    assert dataOut[0]['field3'] == ''

def test_deriveAll_deriveValue_overwriteFalse():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveValue_overwriteFalse, db = db, configName='test_deriveAll_deriveValue_overwriteFalse')
    assert dataOut[0]['field1'] == 'oldvalue'

def test_deriveAll_deriveValue_blankIfNoMatch():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveValue_blankIfNoMatch, db = db, configName='test_deriveAll_deriveValue_blankIfNoMatch')
    assert dataOut[0]['field1'] == ''

# copyValue

def test_deriveAll_copyValue():

    dataOut = dwmAll(data = test_records.record_deriveAll_copyValue, db = db, configName='test_deriveAll_copyValue')
    assert dataOut[0]['field1'] == 'newvalue'

# deriveRegex

def test_deriveAll_deriveRegex_caught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveRegex_caught, db = db, configName='test_deriveAll_deriveRegex')
    assert dataOut[0]['field1'] == 'newvalue'

def test_deriveAll_deriveRegex_uncaught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveRegex_uncaught, db = db, configName='test_deriveAll_deriveRegex')
    assert dataOut[0]['field1'] != 'newvalue'

def test_deriveAll_deriveRegex_notChecked():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveRegex_notChecked, db = db, configName='test_deriveAll_deriveRegex')
    assert dataOut[0]['field3'] == ''

def test_deriveAll_deriveRegex_overwriteFalse():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveRegex_overwriteFalse, db = db, configName='test_deriveAll_deriveRegex_overwriteFalse')
    assert dataOut[0]['field1'] == 'oldvalue'

def test_deriveAll_deriveRegex_blankIfNoMatch():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveRegex_blankIfNoMatch, db = db, configName='test_deriveAll_deriveRegex_blankIfNoMatch')
    assert dataOut[0]['field1'] == ''

# deriveIncludes

def test_deriveAll_deriveIncludes_included_caught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveIncludes_included_caught, db = db, configName='test_deriveAll_deriveIncludes')
    assert dataOut[0]['field1'] == 'goodvalue'

def test_deriveAll_deriveIncludes_included_uncaught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveIncludes_included_uncaught, db = db, configName='test_deriveAll_deriveIncludes')
    assert dataOut[0]['field1'] != 'goodvalue'

def test_deriveAll_deriveIncludes_excluded_caught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveIncludes_excluded_caught, db = db, configName='test_deriveAll_deriveIncludes')
    assert dataOut[0]['field1'] != 'goodvalue'

def test_deriveAll_deriveIncludes_excluded_uncaught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveIncludes_excluded_uncaught, db = db, configName='test_deriveAll_deriveIncludes')
    assert dataOut[0]['field1'] == 'goodvalue'

def test_deriveAll_deriveIncludes_begins_caught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveIncludes_begins_caught, db = db, configName='test_deriveAll_deriveIncludes')
    assert dataOut[0]['field1'] == 'goodvalue'

def test_deriveAll_deriveIncludes_begins_uncaught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveIncludes_begins_uncaught, db = db, configName='test_deriveAll_deriveIncludes')
    assert dataOut[0]['field1'] != 'goodvalue'

def test_deriveAll_deriveIncludes_ends_caught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveIncludes_ends_caught, db = db, configName='test_deriveAll_deriveIncludes')
    assert dataOut[0]['field1'] == 'goodvalue'

def test_deriveAll_deriveIncludes_ends_uncaught():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveIncludes_ends_uncaught, db = db, configName='test_deriveAll_deriveIncludes')
    assert dataOut[0]['field1'] != 'goodvalue'

def test_deriveAll_deriveIncludes_notChecked():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveIncludes_notChecked, db = db, configName='test_deriveAll_deriveIncludes')
    assert dataOut[0]['field2'] != 'goodvalue'

def test_deriveAll_deriveIncludes_overwriteFalse():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveIncludes_overwriteFalse, db = db, configName='test_deriveAll_deriveIncludes_overwriteFalse')
    assert dataOut[0]['field1'] == 'oldvalue'

def test_deriveAll_deriveIncludes_blankIfNoMatch():

    dataOut = dwmAll(data = test_records.record_deriveAll_deriveIncludes_blankIfNoMatch, db = db, configName='test_deriveAll_deriveIncludes_blankIfNoMatch')
    assert dataOut[0]['field1'] == ''

# ensure proper sorting on derive
def test_derive_sort():

    dataOut = dwmAll(data = test_records.record_derive_sort, db = db, configName='test_derive_sort')
    assert dataOut[0]['field1'] == 'correctvalue'

# ensure derive check match
def test_deriveIncludes_deriveCheckMatch():
    dataOut_FirstExecution = dwmAll(data=test_records.history_deriveIncludes_deriveCheckMatch, db=db, configName='test_deriveAll_deriveIncludes_deriveCheckMatch')
    dataOut_SecondExecution = dwmAll(data = dataOut_FirstExecution, db = db, configName='test_deriveAll_deriveIncludes_deriveCheckMatch')
    assert dataOut_FirstExecution[0]['field1'] == dataOut_SecondExecution[0]['field1']

######################################
## test contact history

# genericLookup

def test_history_genericLookup_caught():

    dataOut = dwmAll(data = test_records.history_genericLookup_caught, db = db, configName='test_lookupAll_genericLookup')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['genericLookup']['from'] == 'badvalue'

def test_history_genericLookup_uncaught():

    dataOut = dwmAll(data = test_records.history_genericLookup_uncaught, db = db, configName='test_lookupAll_genericLookup')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_genericLookup_notChecked():

    dataOut = dwmAll(data = test_records.history_genericLookup_notChecked, db = db, configName='test_lookupAll_genericLookup')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field2' not in hist.keys()

# # fieldSpecificLookup

def test_history_fieldSpecificLookup_caught():

    dataOut = dwmAll(data = test_records.history_fieldSpecificLookup_caught, db = db, configName='test_lookupAll_fieldSpecificLookup')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['fieldSpecificLookup']['from'] == 'badvalue'

def test_history_fieldSpecificLookup_uncaught():

    dataOut = dwmAll(data = test_records.history_fieldSpecificLookup_uncaught, db = db, configName='test_lookupAll_fieldSpecificLookup')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_fieldSpecificLookup_notChecked():

    dataOut = dwmAll(data = test_records.history_fieldSpecificLookup_notChecked, db = db, configName='test_lookupAll_fieldSpecificLookup')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field2' not in hist.keys()


# # CurrentFieldLookup
def test_writeContactHistory_currentField():

    dataOut = dwmAll(data = test_records.record_writeContactHistory_writeConfig, db = db, configName='test_writeContactHistory_writeConfig')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['_current'] == 0

def test_writeContactHistory_currentFieldInc():
    # Drop contactHistory before new UT
    db.contactHistory.drop()
    # Create ContactHistory with _currentField
    dataOutOldRec = dwmAll(data=test_records.record_writeContactHistory_historyCurrent1, db=db, configName='test_writeContactHistory_writeConfig')

    # Create new ContactHistory with _currentField and increment old record.
    dataOutNextRec = dwmAll(data=test_records.record_writeContactHistory_historyCurrent2, db=db, configName='test_writeContactHistory_writeConfig')

    # Get old rec with incremented _current
    hist = db.contactHistory.find_one({"_id": dataOutOldRec[0]['historyId']})
    assert hist['_current'] == 1

# normLookup
def test_history_normLookup_caught():

    # do stuff for testing
    dataOut = dwmAll(data = test_records.history_normLookup_caught, db = db, configName='test_lookupAll_normLookup')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['normLookup']['from'] == 'badvalue'

def test_history_normLookup_uncaught():

    dataOut = dwmAll(data = test_records.history_normLookup_uncaught, db = db, configName='test_lookupAll_normLookup')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_normLookup_notChecked():

    dataOut = dwmAll(data = test_records.history_normLookup_notChecked, db = db, configName='test_lookupAll_normLookup')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field2' not in hist.keys()

# normIncludes

def test_history_normIncludes_caught():

    # do stuff for testing
    dataOut = dwmAll(data = test_records.history_normIncludes_included_caught, db = db, configName='test_normIncludes')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['normIncludes']['from'] == 'findgoodinvaluejunk'

def test_history_normIncludes_uncaught():

    dataOut = dwmAll(data = test_records.history_normIncludes_included_uncaught, db = db, configName='test_normIncludes')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_normIncludes_notChecked():

    dataOut = dwmAll(data = test_records.history_normIncludes_notChecked, db = db, configName='test_normIncludes')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field2' not in hist.keys()

# genericRegex

def test_history_genericRegex_caught():

    dataOut = dwmAll(data = test_records.history_genericRegex_caught, db = db, configName='test_regexAll_genericRegex')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['genericRegex']['from'] == 'badvalue'

def test_history_genericRegex_uncaught():

    dataOut = dwmAll(data = test_records.history_genericRegex_uncaught, db = db, configName='test_regexAll_genericRegex')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_genericRegex_notChecked():

    dataOut = dwmAll(data = test_records.history_genericRegex_notChecked, db = db, configName='test_regexAll_genericRegex')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field2' not in hist.keys()

# fieldSpecificRegex

def test_history_fieldSpecificRegex_caught():

    dataOut = dwmAll(data = test_records.history_fieldSpecificRegex_caught, db = db, configName='test_regexAll_fieldSpecificRegex')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['fieldSpecificRegex']['from'] == 'badvalue'

def test_history_fieldSpecificRegex_uncaught():

    dataOut = dwmAll(data = test_records.record_regexAll_fieldSpecificRegex_uncaught, db = db, configName='test_regexAll_fieldSpecificRegex')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_fieldSpecificRegex_notChecked():

    dataOut = dwmAll(data = test_records.history_fieldSpecificRegex_notChecked, db = db, configName='test_regexAll_fieldSpecificRegex')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field2' not in hist.keys()

# normRegex

def test_history_normRegex_caught():

    dataOut = dwmAll(data = test_records.history_normRegex_caught, db = db, configName='test_regexAll_normRegex')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['normRegex']['from'] == 'badvalue'

def test_history_normRegex_uncaught():

    # do stuff for testing
    dataOut = dwmAll(data = test_records.history_normRegex_uncaught, db = db, configName='test_regexAll_normRegex')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_normRegex_notChecked():

    dataOut = dwmAll(data = test_records.history_normRegex_notChecked, db = db, configName='test_regexAll_normRegex')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field2' not in hist.keys()

# deriveValue

def test_history_deriveValue_caught():

    dataOut = dwmAll(data = test_records.history_deriveValue_caught, db = db, configName='test_deriveAll_deriveValue')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['deriveValue']['from'] == ''

def test_history_deriveValue_uncaught():

    dataOut = dwmAll(data = test_records.history_deriveValue_uncaught, db = db, configName='test_deriveAll_deriveValue')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_deriveValue_notChecked():

    dataOut = dwmAll(data = test_records.history_deriveValue_notChecked, db = db, configName='test_deriveAll_deriveValue')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field3' not in hist.keys()

def test_history_deriveValue_overwriteFalse():

    dataOut = dwmAll(data = test_records.history_deriveValue_overwriteFalse, db = db, configName='test_deriveAll_deriveValue_overwriteFalse')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_deriveValue_blankIfNoMatch():

    dataOut = dwmAll(data = test_records.history_deriveValue_blankIfNoMatch, db = db, configName='test_deriveAll_deriveValue_blankIfNoMatch')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['deriveValue']['using']['blankIfNoMatch'] == 'no match found'

# copyValue

def test_history_copyValue():

    dataOut = dwmAll(data = test_records.history_copyValue, db = db, configName='test_deriveAll_copyValue')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['copyValue']['from'] == ''

# deriveRegex

def test_history_deriveRegex_caught():

    dataOut = dwmAll(data = test_records.history_deriveRegex_caught, db = db, configName='test_deriveAll_deriveRegex')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['deriveRegex']['from'] == ''

def test_history_deriveRegex_uncaught():

    dataOut = dwmAll(data = test_records.history_deriveRegex_uncaught, db = db, configName='test_deriveAll_deriveRegex')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_deriveRegex_notChecked():

    dataOut = dwmAll(data = test_records.history_deriveRegex_notChecked, db = db, configName='test_deriveAll_deriveRegex')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field3' not in hist.keys()

def test_history_deriveRegex_overwriteFalse():

    dataOut = dwmAll(data = test_records.history_deriveRegex_overwriteFalse, db = db, configName='test_deriveAll_deriveRegex_overwriteFalse')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_deriveRegex_blankIfNoMatch():

    dataOut = dwmAll(data = test_records.history_deriveRegex_blankIfNoMatch, db = db, configName='test_deriveAll_deriveRegex_blankIfNoMatch')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['deriveRegex']['pattern'] == 'no matching pattern'

# deriveIncludes

def test_history_deriveIncludes_included_caught():

    dataOut = dwmAll(data = test_records.history_deriveIncludes_included_caught, db = db, configName='test_deriveAll_deriveIncludes')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['deriveIncludes']['from'] == ''

def test_history_deriveIncludes_included_uncaught():

    dataOut = dwmAll(data = test_records.history_deriveIncludes_included_uncaught, db = db, configName='test_deriveAll_deriveIncludes')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_deriveIncludes_excluded_caught():

    dataOut = dwmAll(data = test_records.history_deriveIncludes_excluded_caught, db = db, configName='test_deriveAll_deriveIncludes')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_deriveIncludes_excluded_uncaught():

    dataOut = dwmAll(data = test_records.history_deriveIncludes_excluded_uncaught, db = db, configName='test_deriveAll_deriveIncludes')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['deriveIncludes']['from'] == ''

def test_history_deriveIncludes_begins_caught():

    dataOut = dwmAll(data = test_records.history_deriveIncludes_begins_caught, db = db, configName='test_deriveAll_deriveIncludes')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['deriveIncludes']['from'] == ''

def test_history_deriveIncludes_begins_uncaught():

    dataOut = dwmAll(data = test_records.history_deriveIncludes_begins_uncaught, db = db, configName='test_deriveAll_deriveIncludes')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_deriveIncludes_ends_caught():

    dataOut = dwmAll(data = test_records.history_deriveIncludes_ends_caught, db = db, configName='test_deriveAll_deriveIncludes')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['deriveIncludes']['from'] == ''

def test_history_deriveIncludes_ends_uncaught():

    dataOut = dwmAll(data = test_records.history_deriveIncludes_ends_uncaught, db = db, configName='test_deriveAll_deriveIncludes')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_deriveIncludes_notChecked():

    dataOut = dwmAll(data = test_records.history_deriveIncludes_notChecked, db = db, configName='test_deriveAll_deriveIncludes')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field3' not in hist.keys()

def test_history_deriveIncludes_overwriteFalse():

    dataOut = dwmAll(data = test_records.history_deriveIncludes_overwriteFalse, db = db, configName='test_deriveAll_deriveIncludes_overwriteFalse')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert 'field1' not in hist.keys()

def test_history_deriveIncludes_blankIfNoMatch():

    dataOut = dwmAll(data = test_records.history_deriveIncludes_blankIfNoMatch, db = db, configName='test_deriveAll_deriveIncludes_blankIfNoMatch')
    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})
    assert hist['field1']['deriveIncludes']['using']['blankIfNoMatch'] == 'no match found'

#########################################
## Test options around history
# returnHistoryId False

def test_returnHistoryId_False():

    dataOut = dwmAll(data = test_records.record_returnHistoryId_False, db = db, configName='test_returnHistoryId_False')
    assert 'historyId' not in dataOut[0].keys()

def test_writeContactHistory_False():

    dataOut = dwmAll(data = test_records.record_writeContactHistory_False, db = db, configName='test_writeContactHistory_False')
    assert 'historyId' not in dataOut[0].keys()

def test_writeContactHistory_writeConfig():

    dataOut = dwmAll(data = test_records.record_writeContactHistory_writeConfig, db = db, configName='test_writeContactHistory_writeConfig')

    hist = db.contactHistory.find_one({"_id": dataOut[0]['historyId']})

    assert hist['configName'] == 'test_writeContactHistory_writeConfig'

#########################################
## configuration does not exist
@raises(Exception)
def test_configDoesNotExist():

    dataOut = dwmAll(data = test_records.record_configDoesNotExist, db = db, configName='test_configDoesNotExist')

#########################################
# userDefinedFunctions

def test_udf_beforeGenericValidation():

    dataOut = dwmAll(data = test_records.record_udf_beforeGenericValidation, db = db, configName='test_udf_beforeGenericValidation', udfNamespace=__name__)
    assert dataOut[0]['field1'] == 'goodvalue'

def test_udf_beforeGenericRegex():

    dataOut = dwmAll(data = test_records.record_udf_beforeGenericRegex, db = db, configName='test_udf_beforeGenericRegex', udfNamespace=__name__)
    assert dataOut[0]['field1'] == 'goodvalue'

def test_udf_beforeFieldSpecificValidation():

    dataOut = dwmAll(data = test_records.record_udf_beforeFieldSpecificValidation, db = db, configName='test_udf_beforeFieldSpecificValidation', udfNamespace=__name__)
    assert dataOut[0]['field1'] == 'goodvalue'

def test_udf_beforeFieldSpecificRegex():

    dataOut = dwmAll(data = test_records.record_udf_beforeFieldSpecificRegex, db = db, configName='test_udf_beforeFieldSpecificRegex', udfNamespace=__name__)
    assert dataOut[0]['field1'] == 'goodvalue'

def test_udf_beforeNormalization():

    dataOut = dwmAll(data = test_records.record_udf_beforeNormalization, db = db, configName='test_udf_beforeNormalization', udfNamespace=__name__)
    assert dataOut[0]['field1'] == 'goodvalue'

def test_udf_beforeNormalizationRegex():

    dataOut = dwmAll(data = test_records.record_udf_beforeNormalizationRegex, db = db, configName='test_udf_beforeNormalizationRegex', udfNamespace=__name__)
    assert dataOut[0]['field1'] == 'goodvalue'

def test_udf_beforeNormalizationIncludes():

    dataOut = dwmAll(data = test_records.record_udf_beforeNormalizationIncludes, db = db, configName='test_udf_beforeNormalizationIncludes', udfNamespace=__name__)
    assert dataOut[0]['field1'] == 'goodvalue'

def test_udf_beforeDeriveData():

    dataOut = dwmAll(data = test_records.record_udf_beforeDeriveData, db = db, configName='test_udf_beforeDeriveData', udfNamespace=__name__)
    assert dataOut[0]['field1'] == 'goodvalue'

def test_udf_afterProcessing():

    dataOut = dwmAll(data = test_records.record_udf_afterProcessing, db = db, configName='test_udf_afterProcessing', udfNamespace=__name__)
    assert dataOut[0]['field1'] == 'goodvalue'

def test_udf_sort():

    dataOut = dwmAll(data = test_records.record_udf_sort, db = db, configName='test_udf_sort', udfNamespace=__name__)
    assert dataOut[0]['field1'] == 'goodvalue'

######################################
## Test value exceptions in base-level functions
@raises(Exception)
def test_udf_afterProcessing_invalidFcn():

    dataOut = dwmAll(data = test_records.record_udf_afterProcessing_invalidFcn, db = db, configName='test_udf_afterProcessing_invalidFcn', udfNamespace=__name__)

## bad lookup type:
@raises(ValueError)
def test_DataLookup_badType():

    testVal, histObj = cleaning.DataLookup(fieldVal='', db=db, lookupType='badlookup', fieldName='')

# bad regex type:
@raises(ValueError)
def test_RegexLookup_badType():

    testVal, histObj = cleaning.RegexLookup(fieldVal='', db=db, lookupType='badregex', fieldName='')

# multiple deriveCopy inputs:
@raises(Exception)
def test_DeriveDataCopyValue_badType():

    testVal, histObj = cleaning.DeriveDataCopyValue(fieldName='test', deriveInput={"field1": "a", "field2": "b"}, overwrite=True, fieldVal='')

# multiple deriveRegex inputs:
@raises(Exception)
def test_DeriveDataRegex_badType():

    testVal, histObj = cleaning.DeriveDataRegex(fieldName='test', db=db, deriveInput={"field1": "a", "field2": "b"}, overwrite=True, fieldVal='')

# requires config input
@raises(Exception)
def test_dwmAll_requiresConfigInput():

    dataOut = dwmAll(data = test_records.record_dwmAll_noConfig, db = db, udfNamespace=__name__)

# doesn't allow multiple config
@raises(Exception)
def test_dwmAll_requiresOneConfig():

    dataOut = dwmAll(data = test_records.record_dwmAll_noConfig, db = db, config={"configName": "testConfig"}, configName="testConfig", udfNamespace=__name__)

# doesn't allow invalid includes lookupType
@raises(ValueError)
def test_includesLookup_badType():

    testVal, histObj = cleaning.IncludesLookup(fieldVal='', lookupType='badlookup', db = db, fieldName='')

# deriveIncludes requires deriveInput
@raises(ValueError)
def test_includesLookup_requiresDeriveFieldName():

    testVal, histObj = cleaning.IncludesLookup(fieldVal='', lookupType='deriveIncludes', deriveFieldName='test', db = db, fieldName='')

# deriveIncludes requires deriveFieldName
@raises(ValueError)
def test_includesLookup_requiresDeriveFieldName():

    testVal, histObj = cleaning.IncludesLookup(fieldVal='', lookupType='deriveIncludes', deriveInput='test', db = db, fieldName='')

# warns if returned document doesn't match schema
@patch('dwm.cleaning.warnings.warn')
def test_includesLookup_normIncludes_warnOnBadSchema(mock_warnings):

    cleaning.IncludesLookup(fieldVal='1234', lookupType='normIncludes', db = db, fieldName='field100')
    assert(mock_warnings.called)

# warns if returned document doesn't match schema
@patch('dwm.cleaning.warnings.warn')
def test_includesLookup_deriveIncludes_warnOnBadSchema(mock_warnings):

    cleaning.IncludesLookup(fieldVal='', lookupType='deriveIncludes', db = db, fieldName='field100', deriveFieldName='field101', deriveInput={"field101": "abcd"})
    assert(mock_warnings.called)

# warns if returned document doesn't match schema
@patch('dwm.cleaning.warnings.warn')
def test_regexLookup_warnOnBadSchema(mock_warnings):

    cleaning.RegexLookup(fieldVal='', db = db, fieldName="field100", lookupType="fieldSpecificRegex")
    assert(mock_warnings.called)

# warns if returned document doesn't match schema
@patch('dwm.cleaning.warnings.warn')
def test_deriveValue_warnOnBadSchema(mock_warnings):

    cleaning.DeriveDataLookup(fieldName="field100", db = db, deriveInput = {"field101": "abc"})
    assert(mock_warnings.called)

# warns if returned document doesn't match schema
@patch('dwm.cleaning.warnings.warn')
def test_deriveRegex_warnOnBadSchema(mock_warnings):

    cleaning.DeriveDataRegex(fieldName="field100", db = db, deriveInput = {"field101": "abc"}, overwrite=False, fieldVal='')
    assert(mock_warnings.called)
