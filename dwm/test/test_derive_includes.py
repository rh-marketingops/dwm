""" test generic validation lookup function """

import mongomock
#from mock import patch
#from nose.tools import raises
from .test_deriveValue import deriveValue

from dwm import Dwm

# Setup mongomock db

DB = mongomock.MongoClient().db

DB.deriveValue.insert_many({"fieldName": "vertical", "deriveFieldName": "emailAddress", "includes": "", "excludes": "", "begins": "", "ends": ".GOV","replace": "Government"})

# Setup Dwm instance

FIELDS = {
    'vertical': {
        'lookup': [],
        'derive': [
            {
                'type': 'deriveIncludes',
                'fieldSet': ['emailAddress'],
                'options': ['overwrite']
            },
            {
                'type': 'copyValue',
                'fieldSet': ['industry'],
                'options': ['overwrite']
            }
        ]
        }
}

DWM = Dwm(name='test', mongo=DB, fields=FIELDS)


# Let the testing begin
def test_deriveAll_deriveIncludes_included_caught():

    rec = {"emailAddress": "test@test.com", "field1": "", "field2": "findgoodinvaluejunk"}
    rec_out, _ = DWM._derive(rec, {})
    print(rec_out)
    assert rec_out == {'field1' == 'goodvalue'}

'''
def test_dwm_derive_deriveValue_caught():
    """ Ensure generic lookup occurs """
    rec = {"emailAddress": "test@test.com", "field1": "", "field2": "findthis"}
    rec_out, _ = DWM._derive(rec, {}) #pylint: disable=W0212
    print(rec_out)
    assert rec_out == {'field1': 'newvalue'}

def test_dwm_vg_lup_good():
    """ Ensure good value not cleared """
    rec = {'field1': 'GOODVALUE'}
    rec_out, _ = DWM._val_g_lookup(rec, {}) #pylint: disable=W0212
    assert rec_out == rec


def test_dwm_vg_lup_badcln():
    """ Ensure basic lookup occurs and cleans value before """
    rec = {'field1': '  badvalue\r\n  '}
    rec_out, _ = DWM._val_g_lookup(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': ''}


def test_dwm_vg_lup_badmulti():
    """ Ensure lookup occurs on every field in config """
    rec = {'field1': 'BADVALUE', 'field2': 'BADVALUE'}
    rec_out, _ = DWM._val_g_lookup(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': '', 'field2': ''}


def test_dwm_vg_lup_leave():
    """ Ensure lookup does not occur on field not in config """
    rec = {'field1': 'BADVALUE', 'field3': 'BADVALUE'}
    rec_out, _ = DWM._val_g_lookup(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': '', 'field3': 'BADVALUE'}
'''