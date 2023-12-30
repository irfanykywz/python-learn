from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

CREDS_JSON = ''
creds_dict = json.loads(CREDS_JSON)
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets.readonly'
]
creds = service_account.Credentials.from_service_account_info(creds_dict, scopes = SCOPES)
SAMPLE_SPREADSHEET_ID = ''
SAMPLE_RANGE_NAME = ''
service = build('sheets', 'v4', credentials = creds)

# result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
result = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
print(result.get('values'))