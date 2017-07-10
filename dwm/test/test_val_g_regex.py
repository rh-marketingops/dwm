""" test generic validation regex function """

import mongomock
#from mock import patch
#from nose.tools import raises

from dwm import Dwm

# Setup mongomock db

DB = mongomock.MongoClient().db

DB.genericRegex.insert({"pattern": r"^badvalue$"})

# Setup Dwm instance

FIELDS = {
    'field1': {
        'lookup': ['genericRegex'],
        'derive': []
    },
    'field2': {
        'lookup': ['genericRegex'],
        'derive': []
    }
}

DWM = Dwm(name='test', mongo=DB, fields=FIELDS)

# Let the testing begin

def test_dwm_vg_reg_bad():
    """ Ensure generic regex occurs """
    rec = {'field1': 'BADVALUE'}
    rec_out, _ = DWM._val_g_regex(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': ''}

def test_dwm_vg_reg_good():
    """ Ensure good value not cleared """
    rec = {'field1': 'GOODVALUE'}
    rec_out, _ = DWM._val_g_regex(rec, {}) #pylint: disable=W0212
    assert rec_out == rec

def test_dwm_vg_reg_badcln():
    """ Ensure basic regex occurs and cleans value before """
    rec = {'field1': '  badvalue\r\n  '}
    rec_out, _ = DWM._val_g_regex(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': ''}

def test_dwm_vg_reg_badmulti():
    """ Ensure regex occurs on every field in config """
    rec = {'field1': 'BADVALUE', 'field2': 'BADVALUE'}
    rec_out, _ = DWM._val_g_regex(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': '', 'field2': ''}

def test_dwm_vg_reg_leave():
    """ Ensure regex does not occur on field not in config """
    rec = {'field1': 'BADVALUE', 'field3': 'BADVALUE'}
    rec_out, _ = DWM._val_g_regex(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': '', 'field3': 'BADVALUE'}
