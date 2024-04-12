import os.path 
import base64 
import email 
from sys import argv 
import re
import datetime
import json 
from auth import connect_to_gmail_api
import database_helper
from database_helper import db, engine
from constants import READ_ONLY_SCOPE
import sys
from utils import format_received_date
# Define the SCOPES. If modifying it, delete the token.pickle file. 

query = "-filename:jpg -filename:jpeg -filename:png -filename:gif"
# TABLE_NAME = 'emails'



def parse_arguments():
    """
    Pass arguments to either
    initialize DB or fetch emails.
    """
    if len(argv) > 1:
        if  db.inspect(engine).has_table("emails"):
            if argv[1].isnumeric():
                maxResult = argv[1]
                emails, service = get_emails(maxResult)
                process_emails(emails, service)

            else:
                print("Table already exists. Send count of emails to fetch.")
        else:
            if argv[1] == "init":
                database_helper.create_database_table()
            else:
                print("initialize the database. Send argument init")
                exit() 
    else:
        print("Help Text")




def get_emails(maxResult): 
    # Variable creds will store the user access token. 
    # If no valid token found, we will create one. 
     
    service = connect_to_gmail_api(READ_ONLY_SCOPE, "credentials.json")
    # request a list of all the messages 
    result = service.users().messages().list(userId='me', q=query, maxResults=maxResult).execute() 
    # We can also pass maxResults to get any number of emails. Like this: 
    # result = service.users().messages().list(maxResults=200, userId='me').execute() 
    messages = result.get('messages')

    return messages, service


def process_email_headers(headers):
    for header in headers: 
        if header['name'] == 'Subject': 
            subject = header['value'] 
        if header['name'] == 'From': 
            mail_from = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", header['value'].lower())[0]
        if header['name'] == 'Date':
            date = header['value']
        if header['name'] == 'To':
            mail_to = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", header['value'].lower())[0]

    return {"subject": subject, "mail_from": mail_from, "date": date, "mail_to": mail_to}


def process_email_body(payload):
    
    # The Body of the message is in Encrypted format. So, we have to decode it. 
    # Get the data and decode it with base 64 decoder. 
    # print(payload)
    message_body = ""
    if payload['mimeType'] == "multipart/mixed":
        for parts in payload['parts']:
            if parts['mimeType'] == "multipart/alternative":
                for part in parts['parts']:
                    if part['mimeType'] == 'text/plain':
                        message_body = base64.urlsafe_b64decode(part["body"]["data"]).decode('utf-8')
                        break
            elif parts['mimeType'] == 'text/html':
                message_body = base64.urlsafe_b64decode(parts["body"]["data"]).decode('utf-8')
                break
    elif payload["mimeType"] == "text/html":
        message_body = base64.urlsafe_b64decode(payload["body"]["data"]).decode('utf-8')
    elif payload["mimeType"] == "text/plain":
        message_body = base64.urlsafe_b64decode(payload["body"]["data"]).decode('utf-8')
    elif payload["mimeType"] == "multipart/alternative":
        for part in payload["parts"]:
            if part["mimeType"] == "text/plain":
                message_body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                break
        else:
            for part in payload["parts"]:
                if part["mimeType"] == "text/html":
                    message_body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                    break
            else:
                message_body = base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8')
    return message_body




def process_emails(messages, service):

    # messages is a list of dictionaries where each dictionary contains a message id. 

    # iterate through all the messages
    email_count = 0 
    for msg in messages: 
        # Get the message from its id 
        response = service.users().messages().get(userId='me', id=msg['id'], format='full').execute() 
        
        # Get value of 'payload' from dictionary 'response' 
        message_id = response["id"]
        payload = response['payload'] 
        headers = payload['headers']
        
        required_headers = process_email_headers(headers)
        message_body = process_email_body(payload)

        # Look for Subject and Sender Email in the headers 
        email_received_date = format_received_date(required_headers["date"])

        # check if message id already exists
        if not database_helper.check_message_id(message_id):
            # insert fetched email details in table 
            email_count += 1
            print(f"Inserting email: {email_count}")
            database_helper.insert_email_record(subject=required_headers["subject"], 
                                mail_from=required_headers["mail_from"], 
                                mail_to=required_headers["mail_to"], 
                                received_date=email_received_date,
                                message_body=message_body,
                                payload=json.dumps(payload),
                                message_id=message_id)
        else:
            print(f"Mail exists")            

if __name__ == '__main__':
    parse_arguments()
    # get_emails(1)
    
