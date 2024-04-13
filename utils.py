from dateutil import parser

def validate_rules(rules_group):
    group_ctr = 0
    for group in rules_group:
        group_ctr += 1
        if ("select" not in group):
            print(f"'select' not found in group: {group_ctr}")
            return False
        elif (group["select"] not in ["all", "any"]):
            print(f"'select' value should either be 'any' or 'all' for group: {group_ctr}")
            return False
        if ("rules" not in group): 
            print(f"'rules' not found in group: {group_ctr}")
            return False
        elif (len(group["rules"]) == 0):
            print(f"'rules' not found in group: {group_ctr}")
            return False
        elif ("rules" in group) and (len(group["rules"])>0):
            rule_ctr = 0
            for rule in group["rules"]:
                rule_ctr += 1
                if ("field" not in rule) or ("value" not in rule) or ("condition" not in rule):
                    print(f"KEY_RULE_ERROR: one of the required fields missing from group: {group_ctr}, rule: {rule_ctr}")
                    return False
                elif rule["field"] not in ["mail_from", "mail_to", "subject", "body", "email_received_date"]:
                    print(f"VALUE_RULE_ERROR: value of the required fields is not valid, group: {group_ctr}, rule: {rule_ctr}")
                    return False 
                if rule["field"] == "email_received_date":
                    if "unit" not in rule:
                        print(f"DATE_RULE_ERROR: 'unit' dictionary key missing for field email_received_date, group: {group_ctr}, rule: {rule_ctr}")
                        return False
                    if rule["condition"] not in ["greater than", "less than"]:
                        print(f"CONDITION_ERROR: mentioned 'condition' is not valid, group: {group_ctr}, rule: {rule_ctr}")
                        return False
                elif rule["condition"] not in ["contains", "does not contains", "equal to", "does not equal"]:
                    print(f"CONDITION_ERROR: mentioned 'condition' is not valid, group: {group_ctr}, rule: {rule_ctr}")
                    return False

        if ("action" not in group):
            print(f"'ACTION_ERROR:' action key is missing from group: {group_ctr}")
            return False 
        elif ("action" in group):
            if ("command" not in group["action"]) or ("value" not in group["action"]):
                print(f"ACTION_ERROR: value corresponding to 'action' is not valid. group: {group_ctr}")
                return False 
            if (group["action"]["command"] not in ["mark", "move message"]):
                print(f"ACTION_COMMAND_ERROR: mentioned command is not valid. group:{group_ctr}")
                return False
            if (group["action"]["command"] == "mark") and (group["action"]["value"] not in ["read", "unread"]):
                print(f"ACTION_VALUE_ERROR:Invalid value corresponding to command mark. group: {group_ctr}")
                return False
    return True


def format_received_date(date):
    date_object = parser.parse(date).date()
    return date_object 
  