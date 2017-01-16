record_lookupAll_genericLookup_caught = [{"emailAddress": "test@test.com", "field1": "badvalue"}]

record_lookupAll_genericLookup_uncaught = [{"emailAddress": "test@test.com", "field1": "badvalue-uncaught"}]

record_lookupAll_genericLookup_notChecked = [{"emailAddress": "test@test.com", "field2": "badvalue"}]

record_lookupAll_fieldSpecificLookup_caught = [{"emailAddress": "test@test.com", "field1": "badvalue"}]

record_lookupAll_fieldSpecificLookup_uncaught = [{"emailAddress": "test@test.com", "field1": "badvalue-uncaught"}]

record_lookupAll_fieldSpecificLookup_notChecked = [{"emailAddress": "test@test.com", "field2": "badvalue"}]

record_lookupAll_normLookup_caught = [{"emailAddress": "test@test.com", "field1": "badvalue"}]

record_lookupAll_normLookup_uncaught = [{"emailAddress": "test@test.com", "field1": "badvalue-uncaught"}]

record_lookupAll_normLookup_notChecked = [{"emailAddress": "test@test.com", "field2": "badvalue"}]

record_regexAll_genericRegex_caught = [{"emailAddress": "test@test.com", "field1": "badvalue"}]

record_regexAll_genericRegex_uncaught = [{"emailAddress": "test@test.com", "field1": "badvalue-uncaught"}]

record_regexAll_genericRegex_notChecked = [{"emailAddress": "test@test.com", "field2": "badvalue"}]

record_regexAll_fieldSpecificRegex_caught = [{"emailAddress": "test@test.com", "field1": "badvalue"}]

record_regexAll_fieldSpecificRegex_uncaught = [{"emailAddress": "test@test.com", "field1": "badvalue-uncaught"}]

record_regexAll_fieldSpecificRegex_notChecked = [{"emailAddress": "test@test.com", "field2": "badvalue"}]

record_regexAll_normRegex_caught = [{"emailAddress": "test@test.com", "field1": "badvalue"}]

record_regexAll_normRegex_uncaught = [{"emailAddress": "test@test.com", "field1": "badvalue-uncaught"}]

record_regexAll_normRegex_notChecked = [{"emailAddress": "test@test.com", "field2": "badvalue"}]

record_normIncludes_included_caught = [{"emailAddress": "test@test.com", "field1": "findgoodinvaluejunk"}]

record_normIncludes_included_uncaught = [{"emailAddress": "test@test.com", "field1": "nothere"}]

record_normIncludes_excluded_caught = [{"emailAddress": "test@test.com", "field1": "findgoodinvaluejunk butstuffnobad"}]

record_normIncludes_excluded_uncaught = [{"emailAddress": "test@test.com", "field1": "findgoodinvaluejunk uncaught"}]

record_normIncludes_begins_caught = [{"emailAddress": "test@test.com", "field1": "abcdefg"}]

record_normIncludes_begins_uncaught = [{"emailAddress": "test@test.com", "field1": "hijklmnop"}]

record_normIncludes_ends_caught = [{"emailAddress": "test@test.com", "field1": "qrstuvwxyz"}]

record_normIncludes_ends_uncaught = [{"emailAddress": "test@test.com", "field1": "notalpha"}]

record_normIncludes_notChecked = [{"emailAddress": "test@test.com", "field2": "doesnotmatter"}]

record_deriveAll_deriveValue_caught = [{"emailAddress": "test@test.com", "field1": "", "field2": "findthis"}]

record_derive_sort = [{"emailAddress": "test@test.com", "field1": "", "field3": "findthis", "field4": "nofindthis"}]

record_deriveAll_deriveValue_overwriteFalse = [{"emailAddress": "test@test.com", "field1": "oldvalue", "field2": "findthis"}]

record_deriveAll_deriveValue_blankIfNoMatch = [{"emailAddress": "test@test.com", "field1": "oldvalue", "field2": "youwillnotfindthis"}]

record_deriveAll_deriveValue_uncaught = [{"emailAddress": "test@test.com", "field1": "", "field2": "dontfindthis"}]

record_deriveAll_deriveValue_notChecked = [{"emailAddress": "test@test.com", "field3": "", "field2": "findthis"}]

record_deriveAll_copyValue = [{"emailAddress": "test@test.com", "field1": "", "field2": "newvalue"}]

record_deriveAll_deriveRegex_caught = [{"emailAddress": "test@test.com", "field1": "", "field2": "findthis"}]

record_deriveAll_deriveRegex_uncaught = [{"emailAddress": "test@test.com", "field1": "", "field2": "dontfindthis"}]

record_deriveAll_deriveRegex_notChecked = [{"emailAddress": "test@test.com", "field3": "", "field2": "findthis"}]

record_deriveAll_deriveRegex_overwriteFalse = [{"emailAddress": "test@test.com", "field1": "oldvalue", "field2": "findthis"}]

record_deriveAll_deriveRegex_blankIfNoMatch = [{"emailAddress": "test@test.com", "field1": "oldvalue", "field2": "youwillnotfindthis"}]

record_deriveAll_deriveIncludes_included_caught = [{"emailAddress": "test@test.com", "field1": "", "field2": "findgoodinvaluejunk"}]

record_deriveAll_deriveIncludes_included_uncaught = [{"emailAddress": "test@test.com", "field1": "", "field2": "nothere"}]

record_deriveAll_deriveIncludes_excluded_caught = [{"emailAddress": "test@test.com", "field1": "", "field2": "findgoodinvaluejunk butstuffnobad"}]

record_deriveAll_deriveIncludes_excluded_uncaught = [{"emailAddress": "test@test.com", "field1": "", "field2": "findgoodinvaluejunk uncaught"}]

record_deriveAll_deriveIncludes_begins_caught = [{"emailAddress": "test@test.com", "field1": "", "field2": "abcdefg"}]

record_deriveAll_deriveIncludes_begins_uncaught = [{"emailAddress": "test@test.com", "field1": "", "field2": "hijklmnop"}]

record_deriveAll_deriveIncludes_ends_caught = [{"emailAddress": "test@test.com", "field1": "", "field2": "qrstuvwxyz"}]

record_deriveAll_deriveIncludes_ends_uncaught = [{"emailAddress": "test@test.com", "field1": "", "field2": "notalpha"}]

record_deriveAll_deriveIncludes_notChecked = [{"emailAddress": "test@test.com", "field2": "", "field3": "doesnotmatter"}]

record_deriveAll_deriveIncludes_overwriteFalse = [{"emailAddress": "test@test.com", "field1": "oldvalue", "field2": "findgoodinvaluejunk"}]

record_deriveAll_deriveIncludes_blankIfNoMatch = [{"emailAddress": "test@test.com", "field1": "oldvalue", "field2": "nothere"}]
#

history_genericLookup_caught = [{"emailAddress": "test@test.com", "field1": "badvalue"}]

history_genericLookup_uncaught = [{"emailAddress": "test@test.com", "field1": "badvalue-uncaught"}]

history_genericLookup_notChecked = [{"emailAddress": "test@test.com", "field2": "badvalue"}]

history_fieldSpecificLookup_caught = [{"emailAddress": "test@test.com", "field1": "badvalue"}]

history_fieldSpecificLookup_uncaught = [{"emailAddress": "test@test.com", "field1": "badvalue-uncaught"}]

history_fieldSpecificLookup_notChecked = [{"emailAddress": "test@test.com", "field2": "badvalue"}]

history_normLookup_caught = [{"emailAddress": "test@test.com", "field1": "badvalue"}]

history_normLookup_uncaught = [{"emailAddress": "test@test.com", "field1": "badvalue-uncaught"}]

history_normLookup_notChecked = [{"emailAddress": "test@test.com", "field2": "badvalue"}]

history_genericRegex_caught = [{"emailAddress": "test@test.com", "field1": "badvalue"}]

history_genericRegex_uncaught = [{"emailAddress": "test@test.com", "field1": "badvalue-uncaught"}]

history_genericRegex_notChecked = [{"emailAddress": "test@test.com", "field2": "badvalue"}]

history_fieldSpecificRegex_caught = [{"emailAddress": "test@test.com", "field1": "badvalue"}]

history_fieldSpecificRegex_uncaught = [{"emailAddress": "test@test.com", "field1": "badvalue-uncaught"}]

history_fieldSpecificRegex_notChecked = [{"emailAddress": "test@test.com", "field2": "badvalue"}]

history_normRegex_caught = [{"emailAddress": "test@test.com", "field1": "badvalue"}]

history_normRegex_uncaught = [{"emailAddress": "test@test.com", "field1": "badvalue-uncaught"}]

history_normRegex_notChecked = [{"emailAddress": "test@test.com", "field2": "badvalue"}]

history_normIncludes_included_caught = [{"emailAddress": "test@test.com", "field1": "findgoodinvaluejunk"}]

history_normIncludes_included_uncaught = [{"emailAddress": "test@test.com", "field1": "nothere"}]

history_normIncludes_notChecked = [{"emailAddress": "test@test.com", "field2": "doesnotmatter"}]

history_deriveValue_caught = [{"emailAddress": "test@test.com", "field1": "", "field2": "findthis"}]

history_deriveValue_overwriteFalse = [{"emailAddress": "test@test.com", "field1": "oldvalue", "field2": "findthis"}]

history_deriveValue_blankIfNoMatch = [{"emailAddress": "test@test.com", "field1": "oldvalue", "field2": "youwillnotfindthis"}]

history_deriveValue_uncaught = [{"emailAddress": "test@test.com", "field1": "", "field2": "dontfindthis"}]

history_deriveValue_notChecked = [{"emailAddress": "test@test.com", "field3": "", "field2": "findthis"}]

history_copyValue = [{"emailAddress": "test@test.com", "field1": "", "field2": "newvalue"}]

history_deriveRegex_caught = [{"emailAddress": "test@test.com", "field1": "", "field2": "findthis"}]

history_deriveRegex_uncaught = [{"emailAddress": "test@test.com", "field1": "", "field2": "dontfindthis"}]

history_deriveRegex_notChecked = [{"emailAddress": "test@test.com", "field3": "", "field2": "findthis"}]

history_deriveRegex_overwriteFalse = [{"emailAddress": "test@test.com", "field1": "oldvalue", "field2": "findthis"}]

history_deriveRegex_blankIfNoMatch = [{"emailAddress": "test@test.com", "field1": "oldvalue", "field2": "youwillnotfindthis"}]

history_deriveIncludes_included_caught = [{"emailAddress": "test@test.com", "field1": "", "field2": "findgoodinvaluejunk"}]

history_deriveIncludes_included_uncaught = [{"emailAddress": "test@test.com", "field1": "", "field2": "nothere"}]

history_deriveIncludes_excluded_caught = [{"emailAddress": "test@test.com", "field1": "", "field2": "findgoodinvaluejunk butstuffnobad"}]

history_deriveIncludes_excluded_uncaught = [{"emailAddress": "test@test.com", "field1": "", "field2": "findgoodinvaluejunk uncaught"}]

history_deriveIncludes_begins_caught = [{"emailAddress": "test@test.com", "field1": "", "field2": "abcdefg"}]

history_deriveIncludes_begins_uncaught = [{"emailAddress": "test@test.com", "field1": "", "field2": "hijklmnop"}]

history_deriveIncludes_ends_caught = [{"emailAddress": "test@test.com", "field1": "", "field2": "qrstuvwxyz"}]

history_deriveIncludes_ends_uncaught = [{"emailAddress": "test@test.com", "field1": "", "field2": "notalpha"}]

history_deriveIncludes_notChecked = [{"emailAddress": "test@test.com", "field2": "", "field3": "doesnotmatter"}]

history_deriveIncludes_overwriteFalse = [{"emailAddress": "test@test.com", "field1": "oldvalue", "field2": "findgoodinvaluejunk"}]

history_deriveIncludes_blankIfNoMatch = [{"emailAddress": "test@test.com", "field1": "oldvalue", "field2": "nothere"}]

history_deriveIncludes_deriveCheckMatch = [{"emailAddress": "test@test.com", "field1": "", "field2": "findgoodinvaluejunk", "field3":"notright"}]

record_returnHistoryId_False = [{"emailAddress": "test@test.com"}]

record_writeContactHistory_False = [{"emailAddress": "test@test.com"}]

record_writeContactHistory_writeConfig = [{"emailAddress": "test@test.com"}]

record_writeContactHistory_historyCurrent1 = [{"emailAddress": "test@test.com"}]

record_writeContactHistory_historyCurrent2 = [{"emailAddress": "test@test.com"}]

record_configDoesNotExist = [{"emailAddress": "test@test.com"}]

record_udf_beforeGenericValidation = [{"emailAddress": "test@test.com", "field1": ""}]

record_udf_beforeGenericRegex = [{"emailAddress": "test@test.com", "field1": ""}]

record_udf_beforeFieldSpecificValidation = [{"emailAddress": "test@test.com", "field1": ""}]

record_udf_beforeFieldSpecificRegex = [{"emailAddress": "test@test.com", "field1": ""}]

record_udf_beforeNormalization = [{"emailAddress": "test@test.com", "field1": ""}]

record_udf_beforeNormalizationRegex = [{"emailAddress": "test@test.com", "field1": ""}]

record_udf_beforeNormalizationIncludes = [{"emailAddress": "test@test.com", "field1": ""}]

record_udf_beforeDeriveData = [{"emailAddress": "test@test.com", "field1": ""}]

record_udf_afterProcessing = [{"emailAddress": "test@test.com", "field1": ""}]

record_udf_sort = [{"emailAddress": "test@test.com", "field1": ""}]

record_udf_afterProcessing_invalidFcn = [{"emailAddress": "test@test.com", "field1": ""}]

record_dwmAll_noConfig = [{"emailAddress": "test@test.com"}]
