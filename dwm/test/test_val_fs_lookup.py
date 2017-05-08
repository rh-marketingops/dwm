""" test field-specific validation lookup function """

import mongomock
#from mock import patch
#from nose.tools import raises

from dwm import Dwm

# Setup mongomock db

DB = mongomock.MongoClient().db

DB.fieldSpecificLookup.insert({"fieldName": "field1", "find": "BADVALUE"})
DB.fieldSpecificLookup.insert({"fieldName": "field2", "find": "BADVALUE"})

# Setup Dwm instance

FIELDS = {
    'field1': {
        'lookup': ['fieldSpecificLookup'],
        'derive': []
    },
    'field2': {
        'lookup': ['fieldSpecificLookup'],
        'derive': []
    }
}

DWM = Dwm(name='test', mongo=DB, fields=FIELDS)

# Let the testing begin


def test_dwm_vfs_lup_bad():
    """ Ensure field-specific lookup occurs """
    rec = {'field1': 'BADVALUE'}
    rec_out, _ = DWM._val_fs_lookup(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': ''}


def test_dwm_vfs_lup_good():
    """ Ensure good value not cleared by fs """
    rec = {'field1': 'GOODVALUE'}
    rec_out, _ = DWM._val_fs_lookup(rec, {}) #pylint: disable=W0212
    assert rec_out == rec


def test_dwm_vfs_lup_badcln():
    """ Ensure basic fs lookup occurs and cleans value before """
    rec = {'field1': '  badvalue\r\n  '}
    rec_out, _ = DWM._val_fs_lookup(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': ''}


def test_dwm_vfs_lup_badmulti():
    """ Ensure fs lookup occurs on every field in config """
    rec = {'field1': 'BADVALUE', 'field2': 'BADVALUE'}
    rec_out, _ = DWM._val_fs_lookup(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': '', 'field2': ''}


def test_dwm_vfs_lup_leave():
    """ Ensure fs lookup does not occur on field not in config """
    rec = {'field1': 'BADVALUE', 'field3': 'BADVALUE'}
    rec_out, _ = DWM._val_fs_lookup(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': '', 'field3': 'BADVALUE'}
