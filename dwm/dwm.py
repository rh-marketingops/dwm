from pymongo import MongoClient
from datetime import datetime
from tqdm import tqdm
import time
import collections

from .wrappers import lookupAll, DeriveDataLookupAll
from .helpers import _RunUserDefinedFunctions_, _CollectHistory_, _CollectHistoryAgg_

## DWM on a set of contact records
def dwmAll(data, db, configName, udfNamespace=__name__, verbose=False):
    '''
        Multi-record wrapper for dwmOne

        Arguments:
        * data -- list of contact records (dictionaries)
        * db -- PyMongo MongoClient DB instance (i.e., mongoDb = MongoClient('connectionString')['dbName'])
        * configName -- name of configuration to use
        * writeContactHistory -- bool; whether or not to write a before/after snapshot to contactHistory
    '''

    configColl = db['config']

    config = configColl.find_one({"configName": configName})

    if not config:
        raise Exception("configName '" + configName + "' not found in collection 'config'")

    writeContactHistory = config["history"]["writeContactHistory"]
    returnHistoryId = config["history"]["returnHistoryId"]
    returnHistoryField = config["history"]["returnHistoryField"]
    histIdField = config["history"]["histIdField"]

    for field in config["fields"]:

        config["fields"][field]["derive"] = collections.OrderedDict(sorted(config["fields"][field]["derive"].items()))

    for position in config["userDefinedFunctions"]:

        config["userDefinedFunctions"][position] = collections.OrderedDict(sorted(config["userDefinedFunctions"][position].items()))

    if verbose:
        for row in tqdm(data):
            row, historyId = dwmOne(data=row, db=db, config=config, writeContactHistory=writeContactHistory, returnHistoryId=returnHistoryId, histIdField=histIdField, udfNamespace=udfNamespace)
            if returnHistoryId and writeContactHistory:
                row[returnHistoryField] = historyId
    else:
        for row in data:
            row, historyId = dwmOne(data=row, db=db, config=config, writeContactHistory=writeContactHistory, returnHistoryId=returnHistoryId, histIdField=histIdField, udfNamespace=udfNamespace)
            if returnHistoryId and writeContactHistory:
                row[returnHistoryField] = historyId

    return data

## DWM order on a single record

def dwmOne(data, db, config, writeContactHistory=True, returnHistoryId=True, histIdField={"name": "emailAddress", "value": "emailAddress"}, udfNamespace=__name__):

    '''
        Wrapper for individual DWM functions

        Arguments:
        * data -- single data record to clean; key values should map to system field names (i.e., "Job Role" is keyed as "jobRole", the internal DWM name, not "C_Job_Role11", which is the Eloqua name)
        * db -- PyMongo MongoClient DB instance (i.e., mongoDb = MongoClient('connectionString')['dbName'])
        * configName -- name of configuration to use
        * writeContactHistory -- bool; whether or not to write a before/after snapshot to contactHistory
    '''

    # setup history collector
    history = {}

    # get user-defined function config
    udFun = config['userDefinedFunctions']

    ## Get runtime field configuration
    fieldConfig = config['fields']

    ## Run user-defined functions
    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="beforeGenericValidation", namespace=udfNamespace)

    # Run generic validation lookup
    data, history = lookupAll(data=data, configFields=fieldConfig, lookupType='genericLookup', db=db, histObj=history)

    ## Run user-defined functions
    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="beforeGenericRegex", namespace=udfNamespace)

    # Run generic validation regex
    data, history = lookupAll(data=data, configFields=fieldConfig, lookupType='genericRegex', db=db, histObj=history)

    ## Run user-defined functions
    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="beforeFieldSpecificValidation", namespace=udfNamespace)

    # Run field-specific validation lookup
    data, history = lookupAll(data=data, configFields=fieldConfig, lookupType='fieldSpecificLookup', db=db, histObj=history)

    ## Run user-defined functions
    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="beforeFieldSpecificRegex", namespace=udfNamespace)

    # Run field-specific validation regex
    data, history = lookupAll(data=data, configFields=fieldConfig, lookupType='fieldSpecificRegex', db=db, histObj=history)

    ## Run user-defined functions
    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="beforeNormalization", namespace=udfNamespace)

    # Run normalization lookup
    data, history = lookupAll(data=data, configFields=fieldConfig, lookupType='normLookup', db=db, histObj=history)

    ## Run user-defined functions
    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="beforeNormalizationRegex", namespace=udfNamespace)

    # Run normalization regex
    data, history = lookupAll(data=data, configFields=fieldConfig, lookupType='normRegex', db=db, histObj=history)

    ## Run user-defined functions
    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="beforeDeriveData", namespace=udfNamespace)

    # Fill gaps / refresh derived data
    data, history = DeriveDataLookupAll(data=data, configFields=fieldConfig, db=db, histObj=history)

    ## Run user-defined functions
    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="afterProcessing", namespace=udfNamespace)

    # check if need to write contact change history
    if writeContactHistory:
        history['timestamp'] = int(time.time())
        history[histIdField['name']] = data[histIdField['value']]
        history['config'] = config['configName']
        historyId = db['contactHistory'].insert_one(history).inserted_id

    if writeContactHistory and returnHistoryId:
        return data, historyId
    else:
        return data, None
##
