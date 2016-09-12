import mongomock
from nose.tools import *
from dwm import dwmAll

from .test_genericLookup import genericLookup
from .test_fieldSpecificLookup import fieldSpecificLookup
from .test_normLookup import normLookup

from .test_genericRegex import genericRegex
from .test_fieldSpecificRegex import fieldSpecificRegex
from .test_normRegex import normRegex

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

for row in deriveValue:

    db.deriveValue.insert_one(row)

for row in deriveRegex:

    db.deriveRegex.insert_one(row)

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

# ensure proper sorting on derive

def test_derive_sort():

    dataOut = dwmAll(data = test_records.record_derive_sort, db = db, configName='test_derive_sort')
    assert dataOut[0]['field1'] == 'correctvalue'

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
