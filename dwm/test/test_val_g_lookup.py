""" test generic validation lookup function """

import mongomock
#from mock import patch
#from nose.tools import raises

from dwm import Dwm

# Setup mongomock db

DB = mongomock.MongoClient().db

DB.genericLookup.insert({"find": "BADVALUE"})

# Setup Dwm instance

FIELDS = {
    'field1': {
        'lookup': ['genericLookup'],
        'derive': []
    },
    'field2': {
        'lookup': ['genericLookup'],
        'derive': []
    }
}

DWM = Dwm(name='test', mongo=DB, fields=FIELDS)

# Let the testing begin


def test_dwm_vg_lup_bad():
    """ Ensure generic lookup occurs """
    rec = {'field1': 'BADVALUE'}
    rec_out, _ = DWM._val_g_lookup(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': ''}


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
