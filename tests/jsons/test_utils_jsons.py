missing_select = [
    {
        "rules": [{
            "field": "subject",
            "value": "Assignment",
            "condition": "contains"
        }],
        "action": {"command": "mark", "value": "unread"}
    }
]


missing_field = [
    {
        "select": "all",
        "rules": [{
            "value": "Assignment",
            "condition": "contains"
        }],
        "action": {"command": "mark", "value": "unread"}
    }
]

invalid_command = [
    {
        "select": "any",
        "rules": [{
            "field": "subject",
            "value": "Assignment",
            "condition": "contains"
        }],
        "action": {"command": "move", "value": "unread"}
    }
]

valid_rule = [
    {
        "select": "all",
        "rules": [{
            "field": "subject",
            "value": "Assignment",
            "condition": "contains"
        }],
        "action": {"command": "move message", "value": "unread"}
    }
]


invalid_condition = [
    {
        "select": "all",
        "rules": [{
            "field": "subject",
            "value": "Assignment",
            "condition": "equal to"
        },
        {
            "field": "subject",
            "value": "Assignment",
            "condition": "does not equals to"
        }],
        "action": {"command": "move message", "value": "unread"}
    }
]
