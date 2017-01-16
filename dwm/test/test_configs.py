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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
        }
    },
    {
        "configName": "test_normIncludes",
        "fields": {
            "field1": {
                "lookup": ["normIncludes"],
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
                        "options": ["overwrite"]
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
        }
    },
    {
        "configName": "test_deriveAll_deriveValue_blankIfNoMatch",
        "fields": {
            "field1": {
                "lookup": [],
                "derive": {
                    "1": {
                        "type": "deriveValue",
                        "fieldSet": ["field2"],
                        "options": ["overwrite", "blankIfNoMatch"]
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
        }
    },
    {
        "configName": "test_derive_sort",
        "fields": {
            "field1": {
                "lookup": [],
                "derive": {
                    "2": {
                        "type": "deriveValue",
                        "fieldSet": ["field4"],
                        "options": ["overwrite"]
                    },
                    "1": {
                        "type": "deriveValue",
                        "fieldSet": ["field3"],
                        "options": ["overwrite"]
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
                        "options": ["overwrite"]
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
                        "options": ["overwrite"]
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
        }
    },
    {
        "configName": "test_deriveAll_deriveIncludes",
        "fields": {
            "field1": {
                "lookup": [],
                "derive": {
                    "1": {
                        "type": "deriveIncludes",
                        "fieldSet": ["field2"],
                        "options": ["overwrite"]
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
        }
    },
    {
        "configName": "test_deriveAll_deriveIncludes_deriveCheckMatch",
        "fields": {
            "field1": {
                "lookup": [],
                "derive": {
                    "1": {
                        "type": "deriveIncludes",
                        "fieldSet": ["field2"],
                        "options": ["overwrite"]
                    },
                    "2": {
                        "type": "copyValue",
                        "fieldSet": ["field3"],
                        "options": ["overwrite"]
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
        },
        "history": {
            "writeContactHistory": True,
            "returnHistoryId": True,
            "returnHistoryField": "historyId",
            "histIdField": {"name": "field1", "value": "field1"}
        }
    },
    {
        "configName": "test_deriveAll_deriveIncludes_overwriteFalse",
        "fields": {
            "field1": {
                "lookup": [],
                "derive": {
                    "1": {
                        "type": "deriveIncludes",
                        "fieldSet": ["field2"],
                        "options": []
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
        }
    },
    {
        "configName": "test_deriveAll_deriveIncludes_blankIfNoMatch",
        "fields": {
            "field1": {
                "lookup": [],
                "derive": {
                    "1": {
                        "type": "deriveIncludes",
                        "fieldSet": ["field2"],
                        "options": ["overwrite", "blankIfNoMatch"]
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
        }
    },
    {
        "configName": "test_deriveAll_deriveRegex_blankIfNoMatch",
        "fields": {
            "field1": {
                "lookup": [],
                "derive": {
                    "1": {
                        "type": "deriveRegex",
                        "fieldSet": ["field2"],
                        "options": ["overwrite", "blankIfNoMatch"]
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
                        "options": []
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
                        "options": []
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": False,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
      },
        "history": {
          "writeContactHistory": False,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
        }
    },
    {
        "configName": "test_writeContactHistory_writeConfig",
        "fields": {},
        "userDefinedFunctions": {
            "beforeGenericValidation": {},
            "beforeGenericRegex": {},
            "beforeFieldSpecificValidation": {},
            "beforeFieldSpecificRegex": {},
            "beforeNormalization": {},
            "beforeNormalizationRegex": {},
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
        }
    },
    {
        "configName": "test_udf_beforeNormalizationIncludes",
        "fields": {},
        "userDefinedFunctions": {
            "beforeGenericValidation": {},
            "beforeGenericRegex": {},
            "beforeFieldSpecificValidation": {},
            "beforeFieldSpecificRegex": {},
            "beforeNormalization": {},
            "beforeNormalizationRegex": {},
            "beforeNormalizationIncludes": {
                "1": "ex_udf"
            },
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {
                "1": "ex_udf"
            },
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {
                "1": "ex_udf"
            }
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
        }
    },
    {
        "configName": "test_udf_sort",
        "fields": {},
        "userDefinedFunctions": {
            "beforeGenericValidation": {
                "3": "ex_udf",
                "1": "sort_udf_1",
                "2": "sort_udf_2"
            },
            "beforeGenericRegex": {},
            "beforeFieldSpecificValidation": {},
            "beforeFieldSpecificRegex": {},
            "beforeNormalization": {},
            "beforeNormalizationRegex": {},
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {}
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
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
            "beforeNormalizationIncludes": {},
            "beforeDeriveData": {},
            "afterProcessing": {
                "1": "bad_udf"
            }
      },
        "history": {
          "writeContactHistory": True,
          "returnHistoryId": True,
          "returnHistoryField": "historyId",
          "histIdField": {"name": "emailAddress", "value": "emailAddress"}
        }
    }
]
