import json
from sys import argv 

import sqlalchemy as db

import database_helper 
from auth import connect_to_gmail_api
from constants import MODIFY_SCOPE
from utils import validate_rules



service = connect_to_gmail_api(MODIFY_SCOPE, "credentials.json")


def load_labels():
    labels_list = {}
    labels = service.users().labels().list(userId='me').execute()
    for label in labels['labels']:
        labels_list[label['name']] = label["id"]
    return labels_list
 

def mark_read(message_ids):
    """
    message_id: message_id of the email that is UNREAD.
    """
    post_data = {
        "ids":message_ids,
        "removeLabelIds": ["UNREAD"]
    }
    result = service.users().messages().batchModify(userId="me", body=post_data).execute()
    print(f"Marked {len(message_ids)} emails: READ.")
    

def mark_unread(message_ids):
    post_data = {
        "ids": message_ids,
        "addLabelIds": ["UNREAD"]
    }
    result = service.users().messages().batchModify(userId="me", body=post_data).execute()
    print(f"Marked {len(message_ids)} emails: UNREAD.")


def create_label(label_name):
    label = {'name': label_name}
    new_label = service.users().labels().create(userId='me', body=label).execute()
    print(f"created new label: {label_name}")
    return new_label["id"]


def add_label(message_ids, label_name, labels_list):
    if label_name not in labels_list:
        label_id = create_label(label_name)
        labels_list[label_name] = label_id

    post_data = {
        "ids": message_ids,
        "addLabelIds": [labels_list[label_name]]
    }
    result = service.users().messages().batchModify(userId="me", body=post_data).execute()
    print(f"Moved message to label: {label_name}")


def read_json(filename):
    with open(filename) as file:
        rules_data = json.load(file)
        return rules_data


def process_action(group, message_ids,labels):        
        action = group['action']
        if action["command"] == "mark" and action["value"] == "read":
            mark_read(message_ids)
        elif action["command"] == "mark" and action["value"] == "unread":
            mark_unread(message_ids)
        elif action["command"] == "move message":
            add_label(message_ids, action["value"], labels)


def start():
    # pass filename as command line argument.
    if len(argv) > 1:
        filename = argv[1]
        json_data = read_json(filename)
        flag = validate_rules(json_data)
        if flag:
            for group in json_data:
                message_ids = database_helper.dict_to_sqlalchemy_query(group)
                if len(message_ids) > 0:
                    labels = load_labels()
                    process_action(group, message_ids,labels)
                else:
                    print("No matching results for your given condition. Please try again.")
                    exit()
            

if __name__ == '__main__':
    start()
    