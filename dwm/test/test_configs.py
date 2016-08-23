configs = [

    {
        "configName": "test_lookupAll_genericValidation",
        "fields": {
            "field1": {
                "lookup": ["genericLookup"],
                "derive": {}
            }
        },
        "userDefinedFunctions": {
            "beforeGenericValidation": {},
            "beforeGenericRegex": {},
            "beforeFieldSpecificValidation": {},
            "beforeFieldSpecificRegex": {},
            "beforeNormalization": {},
            "beforeNormalizationRegex": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      }
    }


]
