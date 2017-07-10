""" test copy value case of derive function"""

import mongomock

from dwm import Dwm


# Setup mongomock db
DB = mongomock.MongoClient().db


# Setup Dwm instance
FIELDS = {
    "field1": {
        "lookup": [],
        "derive": [
            {
                "type": "copyValue",
                "fieldSet": ["field2"],
                "options": ["overwrite"]
            }
        ]
    }
}

DWM = Dwm(name='test', mongo=DB, fields=FIELDS)


# Let the testing begin
def test_derive_copy_value():
    """ Ensure derive copy value """
    rec = {"emailAddress": "test@test.com", "field1": "", "field2": "newvalue"}
    rec_out, _ = DWM._derive(rec, {})  # pylint: disable=W0212
    assert rec_out['field1'] == 'newvalue'
