derive = [
    {"type": "deriveValue", "fieldName": "field1", "lookupVals": {"field": "field2", "value": "FINDTHIS"}, "value": "newvalue"},
    {"type": "deriveRegex", "fieldName": "field1", "deriveFieldName": "field2", "pattern": "^findthis$", "replace": "newvalue"},
    {"type": "deriveValue", "fieldName": "field1", "lookupVals": {"field": "field4", "value": "NOFINDTHIS"}, "value": "incorrectvalue"},
    {"type": "deriveValue", "fieldName": "field1", "lookupVals": {"field": "field3", "value": "FINDTHIS"}, "value": "correctvalue"}
]
