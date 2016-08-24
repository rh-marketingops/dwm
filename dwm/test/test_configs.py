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
    },
    {
        "configName": "test_deriveAll_deriveRegex_overwriteFalse",
        "fields": {
            "field1": {
                "lookup": [],
                "derive": {
                    "1": {
                        "type": "deriveRegex",
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
    },
    {
        "configName": "test_returnHistoryId_False",
        "fields": {},
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
        "configName": "test_writeContactHistory_False",
        "fields": {},
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
        "configName": "test_udf_beforeGenericValidation",
        "fields": {},
        "userDefinedFunctions": {
            "beforeGenericValidation": {
                "1": "ex_udf"
            },
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
        "configName": "test_udf_beforeGenericRegex",
        "fields": {},
        "userDefinedFunctions": {
            "beforeGenericValidation": {},
            "beforeGenericRegex": {
                "1": "ex_udf"
            },
            "beforeFieldSpecificValidation": {},
            "beforeFieldSpecificRegex": {},
            "beforeNormalization": {},
            "beforeNormalizationRegex": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      }
    },
    {
        "configName": "test_udf_beforeFieldSpecificValidation",
        "fields": {},
        "userDefinedFunctions": {
            "beforeGenericValidation": {},
            "beforeGenericRegex": {},
            "beforeFieldSpecificValidation": {
                "1": "ex_udf"
            },
            "beforeFieldSpecificRegex": {},
            "beforeNormalization": {},
            "beforeNormalizationRegex": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      }
    },
    {
        "configName": "test_udf_beforeFieldSpecificRegex",
        "fields": {},
        "userDefinedFunctions": {
            "beforeGenericValidation": {},
            "beforeGenericRegex": {},
            "beforeFieldSpecificValidation": {},
            "beforeFieldSpecificRegex": {
                "1": "ex_udf"
            },
            "beforeNormalization": {},
            "beforeNormalizationRegex": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      }
    },
    {
        "configName": "test_udf_beforeNormalization",
        "fields": {},
        "userDefinedFunctions": {
            "beforeGenericValidation": {},
            "beforeGenericRegex": {},
            "beforeFieldSpecificValidation": {},
            "beforeFieldSpecificRegex": {},
            "beforeNormalization": {
                "1": "ex_udf"
            },
            "beforeNormalizationRegex": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      }
    },
    {
        "configName": "test_udf_beforeNormalizationRegex",
        "fields": {},
        "userDefinedFunctions": {
            "beforeGenericValidation": {},
            "beforeGenericRegex": {},
            "beforeFieldSpecificValidation": {},
            "beforeFieldSpecificRegex": {},
            "beforeNormalization": {},
            "beforeNormalizationRegex": {
                "1": "ex_udf"
            },
            "beforeDeriveData": {},
            "afterProcessing": {}
      }
    },
    {
        "configName": "test_udf_beforeDeriveData",
        "fields": {},
        "userDefinedFunctions": {
            "beforeGenericValidation": {},
            "beforeGenericRegex": {},
            "beforeFieldSpecificValidation": {},
            "beforeFieldSpecificRegex": {},
            "beforeNormalization": {},
            "beforeNormalizationRegex": {},
            "beforeDeriveData": {
                "1": "ex_udf"
            },
            "afterProcessing": {}
      }
    },
    {
        "configName": "test_udf_afterProcessing",
        "fields": {},
        "userDefinedFunctions": {
            "beforeGenericValidation": {},
            "beforeGenericRegex": {},
            "beforeFieldSpecificValidation": {},
            "beforeFieldSpecificRegex": {},
            "beforeNormalization": {},
            "beforeNormalizationRegex": {},
            "beforeDeriveData": {},
            "afterProcessing": {
                "1": "ex_udf"
            }
      }
    },
    {
        "configName": "test_udf_afterProcessing_invalidFcn",
        "fields": {},
        "userDefinedFunctions": {
            "beforeGenericValidation": {},
            "beforeGenericRegex": {},
            "beforeFieldSpecificValidation": {},
            "beforeFieldSpecificRegex": {},
            "beforeNormalization": {},
            "beforeNormalizationRegex": {},
            "beforeDeriveData": {},
            "afterProcessing": {
                "1": "bad_udf"
            }
      }
    }
]
