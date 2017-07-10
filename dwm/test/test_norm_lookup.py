""" test normalization validation lookup function """

import mongomock
#from mock import patch
#from nose.tools import raises

from dwm import Dwm

# Setup mongomock db

DB = mongomock.MongoClient().db

DB.normLookup.insert({"fieldName": "field1", "find": "BADVALUE", "replace": "goodvalue"})
DB.normLookup.insert({"fieldName": "field2", "find": "BADVALUE", "replace": "goodvalue"})

# Setup Dwm instance

FIELDS = {
    'field1': {
        'lookup': ['normLookup'],
        'derive': []
    },
    'field2': {
        'lookup': ['normLookup'],
        'derive': []
    }
}

DWM = Dwm(name='test', mongo=DB, fields=FIELDS)

# Let the testing begin


def test_dwm_vnorm_lup_bad():
    """ Ensure field-specific lookup occurs """
    rec = {'field1': 'BADVALUE'}
    rec_out, _ = DWM._norm_lookup(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': 'goodvalue'}


def test_dwm_vnorm_lup_good():
    """ Ensure good value not cleared by fs """
    rec = {'field1': 'GOODVALUE'}
    rec_out, _ = DWM._norm_lookup(rec, {}) #pylint: disable=W0212
    assert rec_out == rec


def test_dwm_vnorm_lup_badcln():
    """ Ensure basic fs lookup occurs and cleans value before """
    rec = {'field1': '  badvalue\r\n  '}
    rec_out, _ = DWM._norm_lookup(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': 'goodvalue'}


def test_dwm_vnorm_lup_badmulti():
    """ Ensure fs lookup occurs on every field in config """
    rec = {'field1': 'BADVALUE', 'field2': 'BADVALUE'}
    rec_out, _ = DWM._norm_lookup(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': 'goodvalue', 'field2': 'goodvalue'}


def test_dwm_vnorm_lup_leave():
    """ Ensure fs lookup does not occur on field not in config """
    rec = {'field1': 'BADVALUE', 'field3': 'BADVALUE'}
    rec_out, _ = DWM._norm_lookup(rec, {}) #pylint: disable=W0212
    assert rec_out == {'field1': 'goodvalue', 'field3': 'BADVALUE'}
