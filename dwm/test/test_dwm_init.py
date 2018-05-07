""" test_dwm_init """
import collections
import mongomock
from nose.tools import raises

from dwm import Dwm

# Setup mongomock db

DB = mongomock.MongoClient().db

# Initialization tests


def test_dwm_initialize():
    """ Test that Dwm class initializes with proper object type """
    assert isinstance(Dwm(name='test', mongo=DB), Dwm)


def test_dwm_init_name():
    """ test Dwm class sets name variable """
    assert Dwm(name='test', mongo=DB).name == 'test'


def test_dwm_init_mongo():
    """ test Dwm class sets MongoDB client """
    assert Dwm(name='test', mongo=DB).mongo == DB


def test_dwm_init_default_fields():
    """ test Dwm class initializes with default fields empty """
    assert Dwm(name='test', mongo=DB).fields == {}


def test_dwm_init_default_udf():
    """ test Dwm class initializes with default fields empty """
    assert Dwm(name='test', mongo=DB).udfs == {}

# Initialize with field settings


def test_dwm_init_fields():
    """ test Dwm class initializes with defined field set """
    fields = {
        'field1': {
            'lookup': ['genericLookup', 'genericRegex', 'fieldSpecificRegex',
                       'fieldSpecificLookup', 'normLookup', 'normIncludes'],
            'derive': [
                {
                    'type': 'deriveIncludes',
                    'fieldSet': ['field2'],
                    'options': []
                }
            ]
        }
    }

    assert Dwm(name='test', mongo=DB, fields=fields).fields == fields


def test_dwm_init_order_fields():
    """ test Dwm class initializes with defined field set in specified order"""
    field_order = ['field4', 'field3', 'field2', 'field1']
    fields = {
        'field1': {
            'lookup': ['genericLookup', 'genericRegex', 'fieldSpecificRegex',
                       'fieldSpecificLookup', 'normLookup', 'normIncludes'],
            'derive': [
                {
                    'type': 'deriveIncludes',
                    'fieldSet': ['field2'],
                    'options': []
                }
            ]
        },
        'field3': {
            'lookup': ['genericLookup', 'genericRegex', 'fieldSpecificRegex',
                       'fieldSpecificLookup', 'normLookup', 'normIncludes'],
            'derive': [
                {
                    'type': 'deriveIncludes',
                    'fieldSet': ['field2'],
                    'options': []
                }
            ]
        },
        'field4': {
            'lookup': ['genericLookup', 'genericRegex', 'fieldSpecificRegex',
                       'fieldSpecificLookup', 'normLookup', 'normIncludes'],
            'derive': []
        },
        'field2': {
            'lookup': ['genericLookup', 'genericRegex', 'fieldSpecificRegex',
                       'fieldSpecificLookup', 'normLookup', 'normIncludes'],
            'derive': []
        }
    }
    ordered_fields = collections.OrderedDict()
    for x in field_order:
        ordered_fields.update({x: fields[x]})

    assert Dwm(name='test', mongo=DB, fields=fields, field_order=field_order).fields == ordered_fields


@raises(ValueError)
def test_dwm_init_fields_badlookup():
    """ test Dwm class raises error with bad lookup type """
    fields = {
        'field1': {
            'lookup': ['genericLookup', 'genericRegex', 'fieldSpecificRegex',
                       'fieldSpecificLookup', 'normLookup', 'badlookup'],
            'derive': [
                {
                    'type': 'deriveIncludes',
                    'fieldSet': ['field2'],
                    'options': []
                }
            ]
        }
    }

    Dwm(name='test', mongo=DB, fields=fields)


@raises(ValueError)
def test_dwm_init_fields_badderive():
    """ test Dwm class raises error with bad derive type """
    fields = {
        'field1': {
            'lookup': ['genericLookup', 'genericRegex', 'fieldSpecificRegex',
                       'fieldSpecificLookup', 'normLookup', 'normIncludes'],
            'derive': [
                {
                    'type': 'badderive',
                    'fieldSet': ['field2'],
                    'options': []
                }
            ]
        }
    }

    Dwm(name='test', mongo=DB, fields=fields)


@raises(ValueError)
def test_dwm_init_fields_badopt():
    """ test Dwm class raises error with bad derive option type """
    fields = {
        'field1': {
            'lookup': ['genericLookup', 'genericRegex', 'fieldSpecificRegex',
                       'fieldSpecificLookup', 'normLookup', 'normIncludes'],
            'derive': [
                {
                    'type': 'deriveIncludes',
                    'fieldSet': ['field2'],
                    'options': ['badoption']
                }
            ]
        }
    }

    Dwm(name='test', mongo=DB, fields=fields)


# Initialize with User-Defined Functions

def udf_example_good(data, hist):
    """ example UDF function for testing; has expected parameters """
    return data, hist


def test_dwm_init_udf():
    """ test Dwm class initializes with defined UDFs """
    udf_set = {
        'beforeGenericValLookup': udf_example_good,
        'beforeGenericValRegex': udf_example_good,
        'beforeFieldSpecificLookup': udf_example_good,
        'beforeFieldSpecificRegex': udf_example_good,
        'beforeNormLookup': udf_example_good,
        'beforeNormRegex': udf_example_good,
        'beforeNormIncludes': udf_example_good,
        'beforeDerive': udf_example_good,
        'afterAll': udf_example_good
    }

    assert Dwm(name='test', mongo=DB, udfs=udf_set).udfs == udf_set


@raises(ValueError)
def test_dwm_init_udf_badpos():
    """ test Dwm class raises error with invalid position """

    udf_set = {
        'badposition': udf_example_good
    }

    Dwm(name='test', mongo=DB, udfs=udf_set)
