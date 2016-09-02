import re
import sys

## misc fcns that make everything else go smooth

def _CollectHistory_(lookupType, fromVal, toVal, using='', pattern=''):
    '''
        Create field change history object

        Arguments:
        * type --
        * fromVal --
        * toVal --
        * using --
        * pattern --
    '''

    histObj = {}

    if fromVal != toVal:
        histObj[lookupType] = {"from": fromVal, "to": toVal}

        if lookupType in ['deriveValue', 'deriveRegex', 'copyValue'] and using!='':
            histObj[lookupType]["using"] = using
        if lookupType in ['genericRegex', 'fieldSpecificRegex', 'normRegex', 'deriveRegex'] and pattern!='':
            histObj[lookupType]["pattern"] = pattern

    return histObj

def _CollectHistoryAgg_(contactHist, fieldHistObj, fieldName):
    '''
        Append field change history object into contact history object

        Arguments:
        * contactHist --
        * fieldHistObj --
        * fieldName --
    '''

    if fieldHistObj!={}:
        if fieldName not in contactHist.keys():
            contactHist[fieldName] = {}
        for lookupType in fieldHistObj.keys():
            contactHist[fieldName][lookupType] = fieldHistObj[lookupType]

    return contactHist

def _DataClean_(fieldVal):
    '''
        Apply standard cleaning to a value. Same cleaning will be applied on back-end to lookup tables

        Arguments:
        * fieldVal -- field value to clean
    '''

    fieldValNew = fieldVal

    fieldValNew = fieldValNew.upper()

    fieldValNew = fieldValNew.strip()

    fieldValNew = re.sub("[\s\n\t]+", " ", fieldValNew)

    return fieldValNew

def _RunUserDefinedFunctions_(config, data, histObj, position, namespace=__name__):
    '''
        Given a configuration, run a set of user-defined functions at various positions within DWM logic

        Arguments:
        * config -- DWM configuration object; must contain a 'userDefinedFunctions' dict with dict labels matching the 'position' argument list, and have entries keyed with 1-n function names
        * data -- dictionary of data for a given row
        * histObj -- object to which field change history (if any) should be appended
        * position -- where in the DWM process to run user-defined functions: beforeGenericValidation, beforeGenericRegex, beforeFieldSpecificValidation, beforeFieldSpecificRegex,
            beforeNormalization, beforeNormalizationRegex, beforeDeriveData, afterProcessing
    '''

    udfConfig = config['userDefinedFunctions']

    if position in udfConfig:

        posConfig = udfConfig[position]

        for udf in posConfig.keys():

            posConfigUDF = posConfig[udf]

            data, histObj = getattr(sys.modules[namespace], posConfigUDF)(data=data, histObj=histObj)

    return data, histObj
