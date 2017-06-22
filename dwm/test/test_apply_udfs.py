""" test apply udfs ( user copy value case of derive function"""

import mongomock

from nose.tools import raises

from dwm import Dwm

from dwm.test.test_udf import ex_udf
from dwm.test.test_udf import sort_udf_1
from dwm.test.test_udf import sort_udf_2

# Setup mongomock db
DB = mongomock.MongoClient().db


def setup_dwm_instance(name_str, mongo_obj, udfs_dict):
    """
    set up DWM instance
    :param str name_str: Name of configuration
    :param MongoClient mongo: MongoDB connection
    :param dict udfs: dict of udfs to run
    """

    return Dwm(name=name_str, mongo=mongo_obj, udfs=udfs_dict)


# Let the testing begin
def test_udf_before_generic_validation():
    """ Ensure udf before generic validation """
    # Setup Dwm instance

    udfs_obj = {
        "beforeGenericValLookup": {
            "1": ex_udf
        },
        "beforeGenericValRegex": {},
        "beforeFieldSpecificLookup": {},
        "beforeFieldSpecificRegex": {},
        "beforeNormLookup": {},
        "beforeNormRegex": {},
        "beforeNormIncludes": {},
        "beforeDerive": {},
        "afterAll": {}
    }

    dwm_obj = setup_dwm_instance('test', DB, udfs_obj)

    rec = {"emailAddress": "test@test.com", "field1": ""}
    rec_out, _ = dwm_obj._apply_udfs(rec, {}, 'beforeGenericValLookup') # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_udf_before_generic_regex():
    """ Ensure udf before generic regex """
    udfs_obj = {
        "beforeGenericValLookup": {},
        "beforeGenericValRegex": {
            "1": ex_udf
        },
        "beforeFieldSpecificLookup": {},
        "beforeFieldSpecificRegex": {},
        "beforeNormLookup": {},
        "beforeNormRegex": {},
        "beforeNormIncludes": {},
        "beforeDerive": {},
        "afterAll": {}
    }

    dwm_obj = setup_dwm_instance('test', DB, udfs_obj)

    rec = {"emailAddress": "test@test.com", "field1": ""}
    rec_out, _ = dwm_obj._apply_udfs(rec, {}, 'beforeGenericValRegex') # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_udf_before_field_specific_validation():
    """ Ensure udf before field specific validation """
    udfs_obj = {
        "beforeGenericValLookup": {},
        "beforeGenericValRegex": {},
        "beforeFieldSpecificLookup": {
            "1": ex_udf
        },
        "beforeFieldSpecificRegex": {},
        "beforeNormLookup": {},
        "beforeNormRegex": {},
        "beforeNormIncludes": {},
        "beforeDerive": {},
        "afterAll": {}
    }

    dwm_obj = setup_dwm_instance('test', DB, udfs_obj)

    rec = {"emailAddress": "test@test.com", "field1": ""}
    rec_out, _ = dwm_obj._apply_udfs(rec, {}, 'beforeFieldSpecificLookup') # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_udf_before_field_specific_regex():
    """ Ensure udf before field specific regex """
    udfs_obj = {
        "beforeGenericValLookup": {},
        "beforeGenericValRegex": {},
        "beforeFieldSpecificLookup": {},
        "beforeFieldSpecificRegex": {
            "1": ex_udf
        },
        "beforeNormLookup": {},
        "beforeNormRegex": {},
        "beforeNormIncludes": {},
        "beforeDerive": {},
        "afterAll": {}
    }

    dwm_obj = setup_dwm_instance('test', DB, udfs_obj)

    rec = {"emailAddress": "test@test.com", "field1": ""}
    rec_out, _ = dwm_obj._apply_udfs(rec, {}, 'beforeFieldSpecificRegex') # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_udf_before_normalization():
    """ Ensure udf before normalization """
    udfs_obj = {
        "beforeGenericValLookup": {},
        "beforeGenericValRegex": {},
        "beforeFieldSpecificLookup": {},
        "beforeFieldSpecificRegex": {},
        "beforeNormLookup": {
            "1": ex_udf
        },
        "beforeNormRegex": {},
        "beforeNormIncludes": {},
        "beforeDerive": {},
        "afterAll": {}
    }

    dwm_obj = setup_dwm_instance('test', DB, udfs_obj)

    rec = {"emailAddress": "test@test.com", "field1": ""}
    rec_out, _ = dwm_obj._apply_udfs(rec, {}, 'beforeNormLookup') # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_udf_before_normalization_regex():
    """ Ensure udf before normalization regex"""
    udfs_obj = {
        "beforeGenericValLookup": {},
        "beforeGenericValRegex": {},
        "beforeFieldSpecificLookup": {},
        "beforeFieldSpecificRegex": {},
        "beforeNormLookup": {},
        "beforeNormRegex": {
            "1": ex_udf
        },
        "beforeNormIncludes": {},
        "beforeDerive": {},
        "afterAll": {}
    }

    dwm_obj = setup_dwm_instance('test', DB, udfs_obj)

    rec = {"emailAddress": "test@test.com", "field1": ""}
    rec_out, _ = dwm_obj._apply_udfs(rec, {}, 'beforeNormRegex') # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_udf_before_normalization_includes():
    """ Ensure udf before normalization includes"""
    udfs_obj = {
        "beforeGenericValLookup": {},
        "beforeGenericValRegex": {},
        "beforeFieldSpecificLookup": {},
        "beforeFieldSpecificRegex": {},
        "beforeNormLookup": {},
        "beforeNormRegex": {},
        "beforeNormIncludes": {
            "1": ex_udf
        },
        "beforeDerive": {},
        "afterAll": {}
    }

    dwm_obj = setup_dwm_instance('test', DB, udfs_obj)

    rec = {"emailAddress": "test@test.com", "field1": ""}
    rec_out, _ = dwm_obj._apply_udfs(rec, {}, 'beforeNormIncludes') # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_udf_before_derive_data():
    """ Ensure udf before derive data"""
    udfs_obj = {
        "beforeGenericValLookup": {},
        "beforeGenericValRegex": {},
        "beforeFieldSpecificLookup": {},
        "beforeFieldSpecificRegex": {},
        "beforeNormLookup": {},
        "beforeNormRegex": {},
        "beforeNormIncludes": {},
        "beforeDerive": {
            "1": ex_udf
        },
        "afterAll": {}
    }

    dwm_obj = setup_dwm_instance('test', DB, udfs_obj)

    rec = {"emailAddress": "test@test.com", "field1": ""}
    rec_out, _ = dwm_obj._apply_udfs(rec, {}, 'beforeDerive') # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_udf_after_all():
    """ Ensure udf before derive data"""
    udfs_obj = {
        "beforeGenericValLookup": {},
        "beforeGenericValRegex": {},
        "beforeFieldSpecificLookup": {},
        "beforeFieldSpecificRegex": {},
        "beforeNormLookup": {},
        "beforeNormRegex": {},
        "beforeNormIncludes": {},
        "beforeDerive": {},
        "afterAll": {
            "1": ex_udf
        }
    }

    dwm_obj = setup_dwm_instance('test', DB, udfs_obj)

    rec = {"emailAddress": "test@test.com", "field1": ""}
    rec_out, _ = dwm_obj._apply_udfs(rec, {}, 'afterAll') # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


def test_udf_sort():
    """ Ensure udf sort case"""
    udfs_obj = {
        "beforeGenericValLookup": {
            "3": ex_udf,
            "1": sort_udf_1,
            "2": sort_udf_2
        },
        "beforeGenericValRegex": {},
        "beforeFieldSpecificLookup": {},
        "beforeFieldSpecificRegex": {},
        "beforeNormLookup": {},
        "beforeNormRegex": {},
        "beforeNormIncludes": {},
        "beforeDerive": {},
        "afterAll": {}
    }

    dwm_obj = setup_dwm_instance('test', DB, udfs_obj)

    rec = {"emailAddress": "test@test.com", "field1": ""}
    rec_out, _ = dwm_obj._apply_udfs(rec, {}, 'beforeGenericValLookup') # pylint: disable=W0212
    assert rec_out['field1'] == 'goodvalue'


@raises(Exception)
def test_udf_after_all_invalid_func():
    """ Test value exceptions in base-level functions """
    udfs_obj = {
        "beforeGenericValLookup": {},
        "beforeGenericValRegex": {},
        "beforeFieldSpecificLookup": {},
        "beforeFieldSpecificRegex": {},
        "beforeNormLookup": {},
        "beforeNormRegex": {},
        "beforeNormIncludes": {},
        "beforeDerive": {},
        "afterAll": {
            "1": "bad_udf"
        }
    }

    dwm_obj = setup_dwm_instance('test', DB, udfs_obj)

    rec = {"emailAddress": "test@test.com", "field1": ""}
    _, _ = dwm_obj._apply_udfs(rec, {}, 'afterAll') # pylint: disable=W0212
