from pymongo import MongoClient
from datetime import datetime
import re
from collections import OrderedDict

from .helpers import _CollectHistory_, _CollectHistoryAgg_, _DataClean_

def DataLookup(fieldVal, db, lookupType, fieldName, histObj={}):
    """
    Return new field value based on single-value lookup against MongoDB

    :param string fieldVal: input value to lookup
    :param MongoClient db: MongoClient instance connected to MongoDB
    :param string lookupType: Type of lookup to perform/MongoDB collection name. One of 'genericLookup', 'fieldSpecificLookup', 'normLookup'
    :param string fieldName: Field name to query against
    :param dict histObj: History object to which changes should be appended
    """

    if (lookupType=='genericLookup'):
        lookupDict = {"find": _DataClean_(fieldVal)}
    elif (lookupType in ['fieldSpecificLookup', 'normLookup']):
        lookupDict = {"fieldName": fieldName, "find": _DataClean_(fieldVal)}
    else:
        raise ValueError("Invalid lookupType")

    fieldValNew = fieldVal

    coll = db[lookupType]

    lval = coll.find_one(lookupDict, ['replace'])

    if lval:
        if 'replace' in lval:
            fieldValNew = lval['replace']
        else:
            fieldValNew = ''

    change = _CollectHistory_(lookupType=lookupType, fromVal=fieldVal, toVal=fieldValNew)

    histObjUpd = _CollectHistoryAgg_(contactHist=histObj, fieldHistObj=change, fieldName=fieldName)

    return fieldValNew, histObjUpd


def RegexLookup(fieldVal, db, fieldName, lookupType, histObj={}):
    """
    Return a new field value based on match against regex queried from MongoDB

    :param string fieldVal: input value to lookup
    :param MongoClient db: MongoClient instance connected to MongoDB
    :param string lookupType: Type of lookup to perform/MongoDB collection name. One of 'genericRegex', 'fieldSpecificRegex', 'normRegex'
    :param string fieldName: Field name to query against
    :param dict histObj: History object to which changes should be appended
    """

    if (lookupType=='genericRegex'):
        lookupDict = {}
    elif (lookupType in ['fieldSpecificRegex', 'normRegex']):
        lookupDict = {"fieldName": fieldName}
    else:
        raise ValueError("Invalid type")

    fieldValNew = fieldVal
    pattern = ''

    coll = db[lookupType]

    reVal = coll.find(lookupDict, ['pattern', 'replace'])

    for row in reVal:

        match = re.match(row['pattern'], _DataClean_(fieldValNew), flags=re.IGNORECASE)

        if match:

            if 'replace' in row:
                fieldValNew = re.sub(row['pattern'], row['replace'], _DataClean_(fieldValNew), flags=re.IGNORECASE)
            else:
                fieldValNew = re.sub(row['pattern'], '', _DataClean_(fieldValNew), flags=re.IGNORECASE)

            pattern = row['pattern']
            break

    if reVal:
        reVal.close()

    change = _CollectHistory_(lookupType=lookupType, fromVal=fieldVal, toVal=fieldValNew, pattern=pattern)

    histObjUpd = _CollectHistoryAgg_(contactHist=histObj, fieldHistObj=change, fieldName=fieldName)

    return fieldValNew, histObjUpd

def DeriveDataLookup(fieldName, db, deriveInput, overwrite=True, fieldVal='', histObj={}, blankIfNoMatch=False):
    """
    Return new field value based on single or multi-value lookup against MongoDB

    :param string fieldName: Field name to query against
    :param MongoClient db: MongoClient instance connected to MongoDB
    :param dict deriveInput: Values to perform lookup against: {"lookupField1": "lookupVal1", "lookupField2": "lookupVal2"}
    :param bool overwrite: Should an existing field value be replaced
    :param string fieldVal: Current field value
    :param dict histObj: History object to which changes should be appended
    :param bool blankIfNoMatch: Should field value be set to blank if no match is found
    """

    lookupVals = OrderedDict()

    for val in sorted(deriveInput.keys()):
        lookupVals[val] = _DataClean_(deriveInput[val])

    lookupDict = {}

    lookupDict['fieldName'] = fieldName
    lookupDict['lookupVals'] = lookupVals

    coll = db['deriveValue']

    lval = coll.find_one(lookupDict, ['value'])

    fieldValNew = fieldVal

    deriveUsing = deriveInput

    if lval and (overwrite or (fieldVal=='')):
        fieldValNew = lval['value']
    elif blankIfNoMatch and not lval:
        fieldValNew = ''
        deriveUsing = {'blankIfNoMatch': 'no match found'}

    change = _CollectHistory_(lookupType='deriveValue', fromVal=fieldVal, toVal=fieldValNew, using=deriveUsing)

    histObjUpd = _CollectHistoryAgg_(contactHist=histObj, fieldHistObj=change, fieldName=fieldName)

    return fieldValNew, histObjUpd

def DeriveDataCopyValue(fieldName, deriveInput, overwrite, fieldVal, histObj={}):
    """
    Return new value based on value from another field

    :param string fieldName: Field name to query against
    :param dict deriveInput: Values to perform lookup against: {"copyField1": "copyVal1"}
    :param bool overwrite: Should an existing field value be replaced
    :param string fieldVal: Current field value
    :param dict histObj: History object to which changes should be appended
    """

    if len(deriveInput)>1:
        raise Exception("more than one field/value in deriveInput")

    fieldValNew = fieldVal

    row = list(deriveInput.keys())[0]

    if (deriveInput[row] != '' and (overwrite or (fieldVal==''))):

        fieldValNew = deriveInput[row]

    change = _CollectHistory_(lookupType='copyValue', fromVal=fieldVal, toVal=fieldValNew, using=deriveInput)

    histObjUpd = _CollectHistoryAgg_(contactHist=histObj, fieldHistObj=change, fieldName=fieldName)

    return fieldValNew, histObjUpd

def DeriveDataRegex(fieldName, db, deriveInput, overwrite, fieldVal, histObj={}, blankIfNoMatch=False):
    """
    Return a new field value based on match (of another field) against regex queried from MongoDB

    :param string fieldName: Field name to query against
    :param MongoClient db: MongoClient instance connected to MongoDB
    :param dict deriveInput: Values to perform lookup against: {"lookupField1": "lookupVal1"}
    :param bool overwrite: Should an existing field value be replaced
    :param string fieldVal: Current field value
    :param dict histObj: History object to which changes should be appended
    :param bool blankIfNoMatch: Should field value be set to blank if no match is found
    """

    if len(deriveInput)>1:
        raise Exception("more than one value in deriveInput")

    fieldValNew = fieldVal

    deriveUsing = deriveInput

    row = list(deriveInput.keys())[0]

    pattern = ''

    if (deriveInput[row] != '' and (overwrite or (fieldVal==''))):

        lookupDict = {}

        lookupDict['deriveFieldName'] = row
        lookupDict['fieldName'] = fieldName

        coll = db['deriveRegex']

        reVal = coll.find(lookupDict, ['pattern', 'replace'])

        for lval in reVal:

            match = re.match(lval['pattern'], _DataClean_(deriveInput[row]), flags=re.IGNORECASE)

            if match:

                fieldValNew = re.sub(lval['pattern'], lval['replace'], _DataClean_(deriveInput[row]), flags=re.IGNORECASE)

                pattern = lval['pattern']
                break

        if reVal:
            reVal.close()

        if fieldValNew == fieldVal and blankIfNoMatch:
            fieldValNew = ''
            pattern = 'no matching pattern'
            deriveUsing = {"blankIfNoMatch": "no match found"}

    change = _CollectHistory_(lookupType='deriveRegex', fromVal=fieldVal, toVal=fieldValNew, using=deriveInput, pattern=pattern)

    histObjUpd = _CollectHistoryAgg_(contactHist=histObj, fieldHistObj=change, fieldName=fieldName)

    return fieldValNew, histObjUpd
