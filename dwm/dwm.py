from pymongo import MongoClient
from datetime import datetime
import time

from .wrappers import lookupAll, DeriveDataLookupAll
from .helpers import _RunUserDefinedFunctions_, _CollectHistory_, _CollectHistoryAgg_

## DWM on a set of contact records
def dwmAll(data, mongoDb, mongoConfig, configName, writeContactHistory=True, returnHistoryId=True, returnHistoryField='historyId', histIdField={"name": "emailAddress", "value": "emailAddress"}):
    '''
        Multi-record wrapper for dwmOne

        Arguments:
        * data -- list of contact records (dictionaries)
        * mongoDb -- PyMongo MongoClient DB instance (i.e., mongoDb = MongoClient('connectionString')['dbName'])
        * mongoConfig -- dictionary of mongo collections to reference for the following: config, lookup, regex, derive, contactHistory
        * configName -- name of configuration to use
        * writeContactHistory -- bool; whether or not to write a before/after snapshot to contactHistory
    '''

    configColl = mongoDb[mongoConfig['config']]

    config = configColl.find_one({"configName": configName})

    for row in data:
        row, historyId = dwmOne(data=row, mongoDb=mongoDb, mongoConfig=mongoConfig, config=config, writeContactHistory=writeContactHistory, returnHistoryId=returnHistoryId, histIdField=histIdField)
        if returnHistoryId:
            row[returnHistoryField] = historyId

    return data

## DWM order on a single record

def dwmOne(data, mongoDb, mongoConfig, config, writeContactHistory=True, returnHistoryId=True, histIdField={"name": "emailAddress", "value": "emailAddress"}):

    '''
        Wrapper for individual DWM functions

        Arguments:
        * data -- single data record to clean; key values should map to system field names (i.e., "Job Role" is keyed as "jobRole", the internal DWM name, not "C_Job_Role11", which is the Eloqua name)
        * mongoDb -- PyMongo MongoClient DB instance (i.e., mongoDb = MongoClient('connectionString')['dbName'])
        * mongoConfig -- dictionary of mongo collections to reference for the following: lookup, regex, derive, contactHistory
        * configName -- name of configuration to use
        * writeContactHistory -- bool; whether or not to write a before/after snapshot to contactHistory
    '''

    ## Setup mongo collections using mongoConfig

    lookupColl = mongoDb[mongoConfig['lookup']]

    regexColl = mongoDb[mongoConfig['regex']]

    deriveColl = mongoDb[mongoConfig['derive']]

    contactHistoryColl = mongoDb[mongoConfig['contactHistory']]

    # setup history collector

    history = {}

    # get user-defined function config
    udFun = config['userDefinedFunctions']

    ## Get runtime field configuration

    fieldConfig = config['fields']

    ## Run user-defined functions

    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="beforeGenericValidation")

    # Run generic validation lookup
    data, history = lookupAll(data=data, configFields=fieldConfig, lookupType='genericLookup', coll=lookupColl, histObj=history)

    ## Run user-defined functions

    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="beforeGenericRegex")

    # Run generic validation regex
    data, history = lookupAll(data=data, configFields=fieldConfig, lookupType='genericRegex', coll=regexColl, histObj=history)

    ## Run user-defined functions

    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="beforeFieldSpecificValidation")

    # Run field-specific validation lookup
    data, history = lookupAll(data=data, configFields=fieldConfig, lookupType='fieldSpecificLookup', coll=lookupColl, histObj=history)

    ## Run user-defined functions

    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="beforeFieldSpecificRegex")

    # Run field-specific validation regex
    data, history = lookupAll(data=data, configFields=fieldConfig, lookupType='fieldSpecificRegex', coll=regexColl, histObj=history)

    ## Run user-defined functions

    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="beforeNormalization")

    # Run normalization lookup
    data, history = lookupAll(data=data, configFields=fieldConfig, lookupType='normLookup', coll=lookupColl, histObj=history)

    ## Run user-defined functions

    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="beforeNormalizationRegex")

    # Run normalization regex
    data, history = lookupAll(data=data, configFields=fieldConfig, lookupType='normRegex', coll=regexColl, histObj=history)

    ## Run user-defined functions

    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="beforeDeriveData")

    # Fill gaps / refresh derived data
    data, history = DeriveDataLookupAll(data=data, configFields=fieldConfig, coll=deriveColl, histObj=history)

    ## Run user-defined functions

    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="afterProcessing")

    #print("just finished cleaning for " + data['emailAddress'])

    # check if need to write contact change history
    if writeContactHistory:
        history['timestamp'] = int(time.time())
        history[histIdField['name']] = data[histIdField['value']]
        historyId = contactHistoryColl.insert_one(history).inserted_id

    if writeContactHistory and returnHistoryId:
        return data, historyId
    else:
        return data, None
##
