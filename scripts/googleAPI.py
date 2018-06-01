from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import pandas as pd


class SheetsAPI:

    def __init__(self):
        # Create credentials
        SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
        store = file.Storage('credentials.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('./client_secrets.json', SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build('sheets', 'v4', http=creds.authorize(Http()))

    def get_df(self, sheet_id, sheet_range):
        # Get the values from google sheets
        result = self.service.spreadsheets().values().get(spreadsheetId=sheet_id, range=sheet_range).execute()
        values = result.get('values', [])
        # Convert into a pandas dataframe
        df = pd.DataFrame(values)
        df.columns = df.iloc[0]
        return df[1:]
