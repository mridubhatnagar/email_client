import pickle 
import os 
 
from googleapiclient.discovery import build 
from google_auth_oauthlib.flow import InstalledAppFlow 
from google.auth.transport.requests import Request 


def connect_to_gmail_api(SCOPES, filename):
    creds = None

    # The file token.pickle contains the user access token. 
    # Check if it exists 
    if os.path.exists('token.pickle'): 

        # Read the token from the file and store it in the variable creds 
        with open('token.pickle', 'rb') as token: 
            creds = pickle.load(token)

    # If credentials are not available or are invalid, ask the user to log in. 
    if not creds or not creds.valid: 
        if creds and creds.expired and creds.refresh_token: 
            creds.refresh(Request()) 
        else: 
            flow = InstalledAppFlow.from_client_secrets_file(filename, SCOPES) 
            creds = flow.run_local_server(port=0)
            

    # Save the access token in token.pickle file for the next run 
    with open('token.pickle', 'wb') as token: 
        pickle.dump(creds, token) 

    # Connect to the Gmail API 
    service = build('gmail', 'v1', credentials=creds)
    return service 