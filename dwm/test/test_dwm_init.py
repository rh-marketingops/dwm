""" test_dwm_init """

import mongomock
from mock import patch

from dwm import Dwm

# Setup mongomock db

DB = mongomock.MongoClient().db

# Initialization tests

def test_dwm_initialize():
    """ Test that Dwm class initializes with proper object type """
    dwm = Dwm(name='test', mongo=DB)
    assert isinstance(dwm, Dwm)

def test_dwm_init_name():
    """ test Dwm class sets name variable """
    dwm = Dwm(name='test', mongo=DB)
    assert dwm.name == 'test'

def test_dwm_init_mongo():
    """ test Dwm class sets MongoDB client """
    dwm = Dwm(name='test', mongo=DB)
    assert dwm.mongo == DB

def test_dwm_init_default_fields():
    """ test Dwm class initializes with default fields empty """
    dwm = Dwm(name='test', mongo=DB)
    assert dwm.fields == []

def test_dwm_init_default_udf():
    """ test Dwm class initializes with default fields empty """
    dwm = Dwm(name='test', mongo=DB)
    assert dwm.udfs == []
