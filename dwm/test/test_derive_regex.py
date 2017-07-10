""" test derive regex case of derive function"""

import mongomock

from dwm import Dwm
from .test_deriveRegex import deriveRegex


# Setup mongomock db
DB = mongomock.MongoClient().db

DB.deriveRegex.insert_many(deriveRegex)

# Setup Dwm instance
FIELDS = {
    "field1": {
        "lookup": [],
        "derive": [
            {
                "type": "deriveRegex",
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
                "type": "deriveRegex",
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
                "type": "deriveRegex",
                "fieldSet": ["field2"],
                "options": ["overwrite", "blankIfNoMatch"]
            }
        ]
    }
}

DWM_BLANK_IF_NO_MATCH_OBJ = Dwm(name='test', mongo=DB,
                                fields=FIELDS_BLANK_IF_NO_MATCH)


# Let the testing begin
def test_derive_regex_caught():
    """ Ensure derive regex caught """
    rec = {"emailAddress": "test@test.com", "field1": "", "field2": "findthis"}
    rec_out, _ = DWM._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] == 'newvalue'


def test_derive_regex_uncaught():
    """ Ensure derive regex uncaught """
    rec = {"emailAddress": "test@test.com", "field1": "",
           "field2": "dontfindthis"}
    rec_out, _ = DWM._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] != 'newvalue'


def test_derive_regex_not_checked():
    """ Ensure derive value not checked """
    rec = {"emailAddress": "test@test.com", "field3": "", "field2": "findthis"}
    rec_out, _ = DWM._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field3'] == ''


def test_derive_regex_over_write_false():
    """ Ensure derive value did not over write"""
    rec = {"emailAddress": "test@test.com", "field1": "oldvalue",
           "field2": "findthis"}
    rec_out, _ = DWM_OVERWRITE_FALSE_OBJ._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] == 'oldvalue'


def test_derive_regex_blank_if_no_match():
    """ Ensure derive value did not match if blank"""
    rec = {"emailAddress": "test@test.com", "field1": "oldvalue",
           "field2": "youwillnotfindthis"}
    rec_out, _ = DWM_BLANK_IF_NO_MATCH_OBJ._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] == ''
