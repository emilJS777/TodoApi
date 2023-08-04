user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 3, "maxLength": 60},
        "password": {"type": "string", "minLength": 3, "maxLength": 300},
        "first_name": {"type": "string", "minLength": 3, "maxLength": 9000},
        "last_name": {"type": "string" , "minLength": 3, "maxLength": 9000},
      },
    "required": []
}