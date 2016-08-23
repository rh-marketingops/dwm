configs = [

    {
        "configName": "test_lookupAll_genericLookup",
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
    },
    {
        "configName": "test_lookupAll_fieldSpecificLookup",
        "fields": {
            "field1": {
                "lookup": ["fieldSpecificLookup"],
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
    },
    {
        "configName": "test_lookupAll_normLookup",
        "fields": {
            "field1": {
                "lookup": ["normLookup"],
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
    },
    {
        "configName": "test_regexAll_genericRegex",
        "fields": {
            "field1": {
                "lookup": ["genericRegex"],
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
    },
    {
        "configName": "test_regexAll_fieldSpecificRegex",
        "fields": {
            "field1": {
                "lookup": ["fieldSpecificRegex"],
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
    },
    {
        "configName": "test_regexAll_normRegex",
        "fields": {
            "field1": {
                "lookup": ["normRegex"],
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
    },
    {
        "configName": "test_deriveAll_deriveValue",
        "fields": {
            "field1": {
                "lookup": [],
                "derive": {
                    "1": {
                        "type": "deriveValue",
                        "fieldSet": ["field2"],
                        "overwrite": True
                    }
                }
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
    },
    {
        "configName": "test_deriveAll_copyValue",
        "fields": {
            "field1": {
                "lookup": [],
                "derive": {
                    "1": {
                        "type": "copyValue",
                        "fieldSet": ["field2"],
                        "overwrite": True
                    }
                }
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
    },
    {
        "configName": "test_deriveAll_deriveRegex",
        "fields": {
            "field1": {
                "lookup": [],
                "derive": {
                    "1": {
                        "type": "deriveRegex",
                        "fieldSet": ["field2"],
                        "overwrite": True
                    }
                }
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
    },
    {
        "configName": "test_deriveAll_deriveValue_overwriteFalse",
        "fields": {
            "field1": {
                "lookup": [],
                "derive": {
                    "1": {
                        "type": "deriveValue",
                        "fieldSet": ["field2"],
                        "overwrite": False
                    }
                }
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
