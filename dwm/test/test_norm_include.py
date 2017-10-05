""" test norm include function """

import mongomock

from dwm import Dwm
from .test_normIncludes import normIncludes


# Setup mongomock db
DB = mongomock.MongoClient().db

DB.normIncludes.insert_many(normIncludes)

# Setup Dwm instance
FIELDS = {
    "field1": {
        "lookup": ["normIncludes"],
        "derive": []
    }
}

DWM = Dwm(name='test', mongo=DB, fields=FIELDS)

FIELDS_OVERWRITE_FALSE = {
    "field1": {
        "lookup": [],
        "derive": [
            {
                "type": "deriveValue",
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
                "type": "deriveValue",
                "fieldSet": ["field2"],
                "options": ["overwrite", "blankIfNoMatch"]
            }
        ]
    }
}

DWM_BLANK_IF_NO_MATCH_OBJ = Dwm(name='test', mongo=DB,
                                fields=FIELDS_BLANK_IF_NO_MATCH)


# Let the testing begin
def test_norm_includes_included_caught():
    """ Ensure norm includes included caught """
    rec = {"emailAddress": "test@test.com", "field1": "findgoodinvaluejunk"}
    rec_out, _ = DWM._norm_include(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_norm_includes_included_uncaught():
    """ Ensure norm includes included uncaught """
    rec = {"emailAddress": "test@test.com", "field1": "nothere"}
    rec_out, _ = DWM._norm_include(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] != 'goodvalue'


def test_norm_includes_excluded_caught():
    """ Ensure norm includes excluded caught """
    rec = {"emailAddress": "test@test.com",
           "field1": "findgoodinvaluejunk butstuffnobad"}
    rec_out, _ = DWM._norm_include(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] != 'goodvalue'


def test_norm_includes_excluded_uncaught():
    """ Ensure norm includes excluded uncaught """
    rec = {"emailAddress": "test@test.com",
           "field1": "findgoodinvaluejunk uncaught"}
    rec_out, _ = DWM._norm_include(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_norm_includes_begins_caught():
    """ Ensure norm includes begins caught """
    rec = {"emailAddress": "test@test.com", "field1": "abcdefg"}
    rec_out, _ = DWM._norm_include(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_norm_includes_begins_uncaught():
    """ Ensure norm includes begins uncaught """
    rec = {"emailAddress": "test@test.com", "field1": "hijklmnop"}
    rec_out, _ = DWM._norm_include(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] != 'goodvalue'


def test_norm_includes_ends_caught():
    """ Ensure norm includes ends caught """
    rec = {"emailAddress": "test@test.com", "field1": "qrstuvwxyz"}
    rec_out, _ = DWM._norm_include(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_norm_includes_ends_uncaught():
    """ Ensure norm includes ends uncaught """
    rec = {"emailAddress": "test@test.com", "field1": "notalpha"}
    rec_out, _ = DWM._norm_include(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] != 'goodvalue'


def test_norm_includes_not_checked():
    """ Ensure norm includes not checked """
    rec = {"emailAddress": "test@test.com", "field2": "doesnotmatter"}
    rec_out, _ = DWM._norm_include(rec, {})  # pylint: disable=W0212
    assert rec_out['field2'] != 'goodvalue'
