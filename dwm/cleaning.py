"""
These set of functions are responsible for determining what the new value of a
field should be, in most cases based on a lookup against MongoDB.
"""

import re
import warnings

from collections import OrderedDict

from .helpers import _CollectHistory_
from .helpers import _CollectHistoryAgg_
from .helpers import _DataClean_


def DataLookup(fieldVal, db, lookupType, fieldName, histObj={}):
    """
    Return new field value based on single-value lookup against MongoDB

    :param string fieldVal: input value to lookup
    :param MongoClient db: MongoClient instance connected to MongoDB
    :param string lookupType: Type of lookup to perform/MongoDB collection name.
           One of 'genericLookup', 'fieldSpecificLookup', 'normLookup'
    :param string fieldName: Field name to query against
    :param dict histObj: History object to which changes should be appended
    """

    if lookupType == 'genericLookup':
        lookup_dict = {"find": _DataClean_(fieldVal)}
    elif lookupType in ['fieldSpecificLookup', 'normLookup']:
        lookup_dict = {"fieldName": fieldName, "find": _DataClean_(fieldVal)}
    else:
        raise ValueError("Invalid lookupType")

    field_val_new = fieldVal

    coll = db[lookupType]

    l_val = coll.find_one(lookup_dict, ['replace'])

    if l_val:
        field_val_new = l_val['replace'] if 'replace' in l_val else ''

    change = _CollectHistory_(lookupType=lookupType, fromVal=fieldVal,
                              toVal=field_val_new)

    hist_obj_upd = _CollectHistoryAgg_(contactHist=histObj,
                                       fieldHistObj=change,
                                       fieldName=fieldName)

    return field_val_new, hist_obj_upd


def IncludesLookup(fieldVal, lookupType, db, fieldName, deriveFieldName='',
                   deriveInput={}, histObj={}, overwrite=False,
                   blankIfNoMatch=False):
    """
    Return new field value based on whether or not original value includes AND
    excludes all words in a comma-delimited list queried from MongoDB

    :param string fieldVal: input value to lookup
    :param string lookupType: Type of lookup to perform/MongoDB collection name.
           One of 'normIncludes', 'deriveIncludes'
    :param MongoClient db: MongoClient instance connected to MongoDB
    :param string fieldName: Field name to query against
    :param string deriveFieldName: Field name from which to derive value
    :param dict deriveInput: Values to perform lookup against:
           {"deriveFieldName": "deriveVal1"}
    :param dict histObj: History object to which changes should be appended
    :param bool overwrite: Should an existing field value be replaced
    :param bool blankIfNoMatch: Should field value be set to blank if
           no match is found
    """

    lookup_dict = {
        'fieldName': fieldName
    }

    if lookupType == 'normIncludes':
        field_val_clean = _DataClean_(fieldVal)

    elif lookupType == 'deriveIncludes':

        if deriveFieldName == '' or deriveInput == {}:
            raise ValueError("for 'deriveIncludes' must specify both \
                              'deriveFieldName' and 'deriveInput'")

        lookup_dict['deriveFieldName'] = deriveFieldName
        field_val_clean = _DataClean_(deriveInput[list(deriveInput.keys())[0]])
    else:
        raise ValueError("Invalid lookupType")

    field_val_new = fieldVal
    check_match = False
    using = {}

    coll = db[lookupType]

    inc_val = coll.find(lookup_dict, ['includes', 'excludes', 'begins', 'ends',
                                      'replace'])

    if inc_val and (lookupType == 'normIncludes' or
                    (lookupType == 'deriveIncludes' and
                     (overwrite or fieldVal == ''))):

        for row in inc_val:

            try:

                if (row['includes'] != '' or
                        row['excludes'] != '' or
                        row['begins'] != '' or
                        row['ends'] != ''):

                    if all((a in field_val_clean)
                           for a in row['includes'].split(",")):

                        if all((b not in field_val_clean)
                               for b in row['excludes'].split(",")) \
                                or row['excludes'] == '':

                            if field_val_clean.startswith(row['begins']):

                                if field_val_clean.endswith(row['ends']):

                                    field_val_new = row['replace']

                                    if lookupType == 'deriveIncludes':
                                        using[deriveFieldName] = deriveInput

                                    using['includes'] = row['includes']
                                    using['excludes'] = row['excludes']
                                    using['begins'] = row['begins']
                                    using['ends'] = row['ends']

                                    check_match = True

                                    break

            except KeyError as Key_error_obj:
                warnings.warn('schema error', Key_error_obj)

        if inc_val:
            inc_val.close()

    if (field_val_new == fieldVal and blankIfNoMatch and
            lookupType == 'deriveIncludes'):
        field_val_new = ''
        using['blankIfNoMatch'] = 'no match found'

    change = _CollectHistory_(lookupType=lookupType, fromVal=fieldVal,
                              toVal=field_val_new, using=using)

    histObjUpd = _CollectHistoryAgg_(contactHist=histObj, fieldHistObj=change,
                                     fieldName=fieldName)

    return field_val_new, histObjUpd, check_match


def RegexLookup(fieldVal, db, fieldName, lookupType, histObj={}):
    """
    Return a new field value based on match against regex queried from MongoDB

    :param string fieldVal: input value to lookup
    :param MongoClient db: MongoClient instance connected to MongoDB
    :param string lookupType: Type of lookup to perform/MongoDB collection name.
            One of 'genericRegex', 'fieldSpecificRegex', 'normRegex'
    :param string fieldName: Field name to query against
    :param dict histObj: History object to which changes should be appended
    """

    if lookupType == 'genericRegex':
        lookup_dict = {}
    elif lookupType in ['fieldSpecificRegex', 'normRegex']:
        lookup_dict = {"fieldName": fieldName}
    else:
        raise ValueError("Invalid type")

    field_val_new = fieldVal
    pattern = ''

    coll = db[lookupType]

    re_val = coll.find(lookup_dict, ['pattern', 'replace'])

    for row in re_val:

        try:
            match = re.match(row['pattern'], _DataClean_(field_val_new),
                             flags=re.IGNORECASE)

            if match:

                if 'replace' in row:
                    field_val_new = re.sub(row['pattern'], row['replace'],
                                           _DataClean_(field_val_new),
                                           flags=re.IGNORECASE)
                else:
                    field_val_new = re.sub(row['pattern'], '',
                                           _DataClean_(field_val_new),
                                           flags=re.IGNORECASE)

                pattern = row['pattern']
                break

        except KeyError as Key_error_obj:
            warnings.warn('schema error', Key_error_obj)

    if re_val:
        re_val.close()

    change = _CollectHistory_(lookupType=lookupType, fromVal=fieldVal,
                              toVal=field_val_new, pattern=pattern)

    histObjUpd = _CollectHistoryAgg_(contactHist=histObj, fieldHistObj=change,
                                     fieldName=fieldName)

    return field_val_new, histObjUpd


def DeriveDataLookup(fieldName, db, deriveInput, overwrite=True, fieldVal='',
                     histObj={}, blankIfNoMatch=False):
    """
    Return new field value based on single or multi-value lookup against MongoDB

    :param string fieldName: Field name to query against
    :param MongoClient db: MongoClient instance connected to MongoDB
    :param dict deriveInput: Values to perform lookup against:
           {"lookupField1": "lookupVal1", "lookupField2": "lookupVal2"}
    :param bool overwrite: Should an existing field value be replaced
    :param string fieldVal: Current field value
    :param dict histObj: History object to which changes should be appended
    :param bool blankIfNoMatch: Should field value be set to blank
           if no match is found
    """

    lookup_vals = OrderedDict()

    for val in sorted(deriveInput.keys()):
        lookup_vals[val] = _DataClean_(deriveInput[val])

    lookup_dict = {
        'fieldName': fieldName,
        'lookupVals': lookup_vals
    }

    coll = db['deriveValue']

    l_val = coll.find_one(lookup_dict, ['value'])

    field_val_new = fieldVal

    derive_using = deriveInput

    # If match found return True else False
    check_match = True if l_val else False

    if l_val and (overwrite or (fieldVal == '')):

        try:
            field_val_new = l_val['value']
        except KeyError as Key_error_obj:
            warnings.warn('schema error', Key_error_obj)

    elif blankIfNoMatch and not l_val:

        field_val_new = ''
        derive_using = {'blankIfNoMatch': 'no match found'}

    change = _CollectHistory_(lookupType='deriveValue', fromVal=fieldVal,
                              toVal=field_val_new, using=derive_using)

    hist_obj_upd = _CollectHistoryAgg_(contactHist=histObj, fieldHistObj=change,
                                       fieldName=fieldName)

    return field_val_new, hist_obj_upd, check_match


def DeriveDataCopyValue(fieldName, deriveInput, overwrite, fieldVal, histObj={}):
    """
    Return new value based on value from another field

    :param string fieldName: Field name to query against
    :param dict deriveInput: Values to perform lookup against:
           {"copyField1": "copyVal1"}
    :param bool overwrite: Should an existing field value be replaced
    :param string fieldVal: Current field value
    :param dict histObj: History object to which changes should be appended
    """

    if len(deriveInput) > 1:
        raise Exception("more than one field/value in deriveInput")

    field_val_new = fieldVal

    row = list(deriveInput.keys())[0]

    if deriveInput[row] != '' and (overwrite or (fieldVal == '')):
        field_val_new = deriveInput[row]
        check_match = True
    else:
        check_match = False

    change = _CollectHistory_(lookupType='copyValue', fromVal=fieldVal,
                              toVal=field_val_new, using=deriveInput)

    hist_obj_upd = _CollectHistoryAgg_(contactHist=histObj, fieldHistObj=change,
                                       fieldName=fieldName)

    return field_val_new, hist_obj_upd, check_match


def DeriveDataRegex(fieldName, db, deriveInput, overwrite, fieldVal, histObj={},
                    blankIfNoMatch=False):
    """
    Return a new field value based on match (of another field) against regex
    queried from MongoDB

    :param string fieldName: Field name to query against
    :param MongoClient db: MongoClient instance connected to MongoDB
    :param dict deriveInput: Values to perform lookup against:
           {"lookupField1": "lookupVal1"}
    :param bool overwrite: Should an existing field value be replaced
    :param string fieldVal: Current field value
    :param dict histObj: History object to which changes should be appended
    :param bool blankIfNoMatch: Should field value be set to blank
           if no match is found
    """

    if len(deriveInput) > 1:
        raise Exception("more than one value in deriveInput")

    field_val_new = fieldVal
    check_match = False

    # derive_using = deriveInput

    row = list(deriveInput.keys())[0]

    pattern = ''

    if deriveInput[row] != '' and (overwrite or (fieldVal == '')):

        lookup_dict = {
            'deriveFieldName': row,
            'fieldName': fieldName
        }

        coll = db['deriveRegex']

        re_val = coll.find(lookup_dict, ['pattern', 'replace'])

        for l_val in re_val:

            try:

                match = re.match(l_val['pattern'],
                                 _DataClean_(deriveInput[row]),
                                 flags=re.IGNORECASE)

                if match:

                    field_val_new = re.sub(l_val['pattern'], l_val['replace'],
                                           _DataClean_(deriveInput[row]),
                                           flags=re.IGNORECASE)

                    pattern = l_val['pattern']

                    check_match = True
                    break

            except KeyError as key_error_obj:
                warnings.warn('schema error', key_error_obj)

        if re_val:
            re_val.close()

        if field_val_new == fieldVal and blankIfNoMatch:
            field_val_new = ''
            pattern = 'no matching pattern'
            # derive_using = {"blankIfNoMatch": "no match found"}

    change = _CollectHistory_(lookupType='deriveRegex', fromVal=fieldVal,
                              toVal=field_val_new, using=deriveInput,
                              pattern=pattern)

    hist_obj_upd = _CollectHistoryAgg_(contactHist=histObj, fieldHistObj=change,
                                       fieldName=fieldName)

    return field_val_new, hist_obj_upd, check_match
