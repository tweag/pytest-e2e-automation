from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path
import base64
from bs4 import BeautifulSoup
import json

# Define the SCOPES. If modifying it, delete the token.pickle file.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def getEmails():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
        with open('cred.json', 'r') as infile:
            my_data = json.load(infile)

    if not creds.valid:
        try:
            creds.refresh(Request())
        except:
            print("Try to refresh token Failed")

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            flow = InstalledAppFlow.from_client_secrets_file('cred.json', SCOPES)
            creds = flow.run_local_server(port=0)
        else:
            flow = InstalledAppFlow.from_client_secrets_file('cred.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
        my_data['installed']['refresh_token'] = creds.refresh_token
        with open('cred.json', 'w') as outfile:
            json.dump(my_data, outfile, indent=4)
    service = build('gmail', 'v1', credentials=creds)

    result = service.users().messages().list(userId='me').execute()

    messages = result.get('messages')
    counter = 0
    for msg in messages:
        if counter > 10:
            break
        counter = counter + 1
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()

        try:
            payload = txt['payload']
            headers = payload['headers']

            for d in headers:
                if d['name'] == 'Subject':
                    subject = d['value']
                if d['name'] == 'From':
                    sender = d['value']
                if d['name'] == 'To':
                    receiver = d['value']

            parts = payload.get('parts')[0]
            data = parts['body']['data']
            data = data.replace("-", "+").replace("_", "/")
            decoded_data = base64.b64decode(data)
            soup = BeautifulSoup(decoded_data, "lxml")
            body = soup.body()
            print("Subject: ", subject)
            print("From: ", sender)
            print("To: ", receiver)
            print("Message: ", body)
            print('\n')
        except:
            pass


getEmails()
