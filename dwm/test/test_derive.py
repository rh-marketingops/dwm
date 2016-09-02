derive = [
    {"type": "deriveValue", "fieldName": "field1", "lookupVals": {"field2": "FINDTHIS"}, "value": "newvalue"},
    {"type": "deriveRegex", "fieldName": "field1", "deriveFieldName": "field2", "pattern": "^findthis$", "replace": "newvalue"},
    {"type": "deriveValue", "fieldName": "field1", "lookupVals": {"field4": "NOFINDTHIS"}, "value": "correctvalue"}
]
