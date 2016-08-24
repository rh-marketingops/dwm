regex = [
    {"type": "genericRegex", "pattern": r"^badvalue$"},
    {"type": "fieldSpecificRegex", "fieldName": "field1", "pattern": r"^badvalue$"},
    {"type": "normRegex", "fieldName": "field1", "pattern": r"^badvalue$", "replace": "goodvalue"}
]
