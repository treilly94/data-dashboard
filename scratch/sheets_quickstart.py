"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
based on this tutorial https://developers.google.com/sheets/api/quickstart/python#step_3_set_up_the_sample
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('./client_secrets.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

# Call the Sheets API
SPREADSHEET_ID = '1a5taxJnVBzQXxUPz5cHRgFxfBUmIoFMh28HEVopJV38'
RANGE_NAME = 'EJ17EKG'
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                             range=RANGE_NAME).execute()
values = result.get('values', [])
if not values:
    print('No data found.')
else:
    print(values)