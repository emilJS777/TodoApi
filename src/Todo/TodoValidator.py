todo_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 1, "maxLength": 120},
        "description": {"type": "string", "minLength": 1, "maxLength": 2000},
        "priority": {"type": "number"},
      },
    "required": []
}