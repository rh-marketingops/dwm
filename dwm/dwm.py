from pymongo import MongoClient
from datetime import datetime
from tqdm import tqdm
import time
from collections import OrderedDict

from .wrappers import lookupAll, DeriveDataLookupAll
from .helpers import _RunUserDefinedFunctions_, _CollectHistory_, _CollectHistoryAgg_

## DWM on a set of contact records
def dwmAll(data, db, configName='', config={}, udfNamespace=__name__, verbose=False):
    """
    Return list of dictionaries after cleaning rules have been applied; optionally with a history record ID appended.

    :param list data: list of dictionaries (records) to which cleaning rules should be applied
    :param MongoClient db: MongoDB connection
    :param string configName: name of configuration to use; will be queried from 'config' collection of MongoDB
    :param OrderedDict config: pre-queried config dict
    :param namespace udfNamespace: namespace of current working script; must be passed if using user-defined functions
    :param bool verbose: use tqdm to display progress of cleaning records
    """

    if config=={} and configName=='':
        raise Exception("Please either specify configName or pass a config")

    if config!={} and configName!='':
        raise Exception("Please either specify configName or pass a config")

    if config=={}:
        configColl = db['config']

        config = configColl.find_one({"configName": configName})

        if not config:
            raise Exception("configName '" + configName + "' not found in collection 'config'")

    writeContactHistory = config["history"]["writeContactHistory"]
    returnHistoryId = config["history"]["returnHistoryId"]
    returnHistoryField = config["history"]["returnHistoryField"]
    histIdField = config["history"]["histIdField"]

    for field in config["fields"]:

        config["fields"][field]["derive"] = OrderedDict(sorted(config["fields"][field]["derive"].items()))

    for position in config["userDefinedFunctions"]:

        config["userDefinedFunctions"][position] = OrderedDict(sorted(config["userDefinedFunctions"][position].items()))

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
    """
    Return a single dictionary (record) after cleaning rules have been applied; optionally insert history record to collection 'contactHistory'

    :param dict data: single record (dictionary) to which cleaning rules should be applied
    :param MongoClient db: MongoClient instance connected to MongoDB
    :param dict config: DWM configuration (see DataDictionary)
    :param bool writeContactHistory: Write field-level change history to collection 'contactHistory'
    :param bool returnHistoryId: If writeContactHistory, return '_id' of history record
    :param dict histIdField: Name of identifier for history record: {"name": "emailAddress", "value": "emailAddress"}
    :param namespace udfNamespace: namespace of current working script; must be passed if using user-defined functions
    """

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
    data, history = _RunUserDefinedFunctions_(config=config, data=data, histObj=history, position="beforeNormalizationIncludes", namespace=udfNamespace)

    # Run normalization includes
    data, history = lookupAll(data=data, configFields=fieldConfig, lookupType='normIncludes', db=db, histObj=history)

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
        history['configName'] = config['configName']

        # Set _current value for most recent contact
        history['_current'] = 0
       
        # Increment all _current
        db['contactHistory'].update({histIdField['name']: data[histIdField['value']]}, {'$inc': {'_current': 1}}, multi=True)

        # Insert into DB
        historyId = db['contactHistory'].insert_one(history).inserted_id

    if writeContactHistory and returnHistoryId:
        return data, historyId
    else:
        return data, None
##
