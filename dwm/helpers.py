import re
import sys

## misc fcns that make everything else go smooth

def _CollectHistory_(lookupType, fromVal, toVal, using={}, pattern=''):
    """
    Return a dictionary detailing what, if any, change was made to a record field

    :param string lookupType: what cleaning rule made the change; one of: genericLookup, genericRegex, fieldSpecificLookup, fieldSpecificRegex, normLookup, normRegex, normIncludes, deriveValue, copyValue, deriveRegex
    :param string fromVal: previous field value
    :param string toVal: new string value
    :param dict using: field values used to derive new values; only applicable for deriveValue, copyValue, deriveRegex
    :param string pattern: which regex pattern was matched to make the change; only applicable for genericRegex, fieldSpecificRegex, deriveRegex
    """

    histObj = {}

    if fromVal != toVal:
        histObj[lookupType] = {"from": fromVal, "to": toVal}

        if lookupType in ['deriveValue', 'deriveRegex', 'copyValue', 'normIncludes', 'deriveIncludes'] and using!='':
            histObj[lookupType]["using"] = using
        if lookupType in ['genericRegex', 'fieldSpecificRegex', 'normRegex', 'deriveRegex'] and pattern!='':
            histObj[lookupType]["pattern"] = pattern

    return histObj

def _CollectHistoryAgg_(contactHist, fieldHistObj, fieldName):
    """
    Return updated history dictionary with new field change

    :param dict contactHist: Existing contact history dictionary
    :param dict fieldHistObj: Output of _CollectHistory_
    :param string fieldName: field name
    """

    if fieldHistObj!={}:
        if fieldName not in contactHist.keys():
            contactHist[fieldName] = {}
        for lookupType in fieldHistObj.keys():
            contactHist[fieldName][lookupType] = fieldHistObj[lookupType]

    return contactHist

def _DataClean_(fieldVal):
    """
    Return 'cleaned' value to standardize lookups (convert to uppercase, remove leading/trailing whitespace, carriage returns, line breaks, and unprintable characters)

    :param string fieldVal: field value
    """

    fieldValNew = fieldVal

    fieldValNew = fieldValNew.upper()

    fieldValNew = fieldValNew.strip()

    fieldValNew = re.sub("[\s\n\t]+", " ", fieldValNew)

    return fieldValNew

def _RunUserDefinedFunctions_(config, data, histObj, position, namespace=__name__):
    """
    Return a single updated data record and history object after running user-defined functions

    :param dict config: DWM configuration (see DataDictionary)
    :param dict data: single record (dictionary) to which user-defined functions should be applied
    :param dict histObj: History object to which changes should be appended
    :param string position: position name of which function set from config should be run
    :param namespace: namespace of current working script; must be passed if using user-defined functions
    """

    udfConfig = config['userDefinedFunctions']

    if position in udfConfig:

        posConfig = udfConfig[position]

        for udf in posConfig.keys():

            posConfigUDF = posConfig[udf]

            data, histObj = getattr(sys.modules[namespace], posConfigUDF)(data=data, histObj=histObj)

    return data, histObj
