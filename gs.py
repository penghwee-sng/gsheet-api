from pprint import pprint
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Connect to Google Sheets
scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(".settings/cred.json", scope)
client = gspread.authorize(credentials)

# Open the spreadsheet
sheet = client.open("Users").sheet1

# Get all records from the spreadsheet
data = sheet.get_all_records()
pprint(pd.DataFrame(data))

# Append a new record to the spreadsheet at the bottom of the sheet
sheet.insert_row([f"TestUser{len(data)+2}", 1234567], index=len(data)+2)
