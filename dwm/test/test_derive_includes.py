""" test derive includes case of derive function"""

import mongomock

from dwm import Dwm
from .test_deriveIncludes import deriveIncludes


# Setup mongomock db
DB = mongomock.MongoClient().db

DB.deriveIncludes.insert_many(deriveIncludes)

# Setup Dwm instance
FIELDS = {
    "field1": {
        "lookup": [],
        "derive": [
            {
                "type": "deriveIncludes",
                "fieldSet": ["field2"],
                "options": ["overwrite"]
            }
        ]
    }
}


DWM = Dwm(name='test', mongo=DB, fields=FIELDS)

FIELDS_OVERWRITE_FALSE = {
    "field1": {
        "lookup": [],
        "derive": [
            {
                "type": "deriveIncludes",
                "fieldSet": ["field2"],
                "options": []
            }
        ]
    }
}

DWM_OVERWRITE_FALSE_OBJ = Dwm(name='test', mongo=DB,
                              fields=FIELDS_OVERWRITE_FALSE)

FIELDS_BLANK_IF_NO_MATCH = {
    "field1": {
        "lookup": [],
        "derive": [
            {
                "type": "deriveIncludes",
                "fieldSet": ["field2"],
                "options": ["overwrite", "blankIfNoMatch"]
            }
        ]
    }
}

DWM_BLANK_IF_NO_MATCH_OBJ = Dwm(name='test', mongo=DB,
                                fields=FIELDS_BLANK_IF_NO_MATCH)


# Let the testing begin
def test_derive_includes_included_caught():
    """ Ensure derive includes caught """
    rec = {"emailAddress": "test@test.com", "field1": "",
           "field2": "findgoodinvaluejunk"}
    rec_out, _ = DWM._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_derive_includes_included_uncaught():
    """ Ensure derive includes uncaught """
    rec = {"emailAddress": "test@test.com", "field1": "", "field2": "nothere"}
    rec_out, _ = DWM._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] != 'goodvalue'


def test_derive_includes_excluded_caught():
    """ Ensure derive includes excluded caught """
    rec = {"emailAddress": "test@test.com", "field1": "",
           "field2": "findgoodinvaluejunk butstuffnobad"}
    rec_out, _ = DWM._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] != 'goodvalue'


def test_derive_includes_excluded_uncaught():
    """ Ensure derive includes excluded uncaught """
    rec = {"emailAddress": "test@test.com", "field1": "",
           "field2": "findgoodinvaluejunk uncaught"}
    rec_out, _ = DWM._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_derive_includes_begins_caught():
    """ Ensure derive includes begins caught """
    rec = {"emailAddress": "test@test.com", "field1": "", "field2": "abcdefg"}
    rec_out, _ = DWM._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_derive_includes_begins_uncaught():
    """ Ensure derive includes begins uncaught """
    rec = {"emailAddress": "test@test.com", "field1": "", "field2": "hijklmnop"}
    rec_out, _ = DWM._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] != 'goodvalue'


def test_derive_includes_ends_caught():
    """ Ensure derive includes ends caught """
    rec = {"emailAddress": "test@test.com", "field1": "",
           "field2": "qrstuvwxyz"}
    rec_out, _ = DWM._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_derive_includes_ends_uncaught():
    """ Ensure derive includes ends uncaught """
    rec = {"emailAddress": "test@test.com", "field1": "", "field2": "notalpha"}
    rec_out, _ = DWM._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] != 'goodvalue'


def test_derive_includes_not_checked():
    """ Ensure derive includes not checked """
    rec = {"emailAddress": "test@test.com", "field2": "",
           "field3": "doesnotmatter"}
    rec_out, _ = DWM._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field2'] != 'goodvalue'


def test_derive_includes_over_write_false():
    """ Ensure derive includes over write false"""
    rec = {"emailAddress": "test@test.com", "field1": "oldvalue",
           "field2": "findgoodinvaluejunk"}
    rec_out, _ = DWM_OVERWRITE_FALSE_OBJ._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] == 'oldvalue'


def test_derive_includes_blank_if_no_match():
    """ Ensure derive includes blank if no match"""
    rec = {"emailAddress": "test@test.com", "field1": "oldvalue",
           "field2": "nothere"}
    rec_out, _ = DWM_BLANK_IF_NO_MATCH_OBJ._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] == ''
