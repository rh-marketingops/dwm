""" test_dwm_init """

import mongomock
from mock import patch

from dwm import Dwm

# Initialization tests

def test_dwm_initialize():
    """ Test that Dwm class initializes with proper object type """
    dwm = Dwm()
    assert isinstance(dwm, Dwm)
