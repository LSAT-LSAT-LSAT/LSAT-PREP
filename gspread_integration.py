
# 📎 Google Sheets Integration Stub

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def log_score_to_sheets(score_entry):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("google_creds.json", scope)
    client = gspread.authorize(creds)

    # Replace with your actual sheet name
    sheet = client.open("LSAT_Study_Tracker").sheet1
    sheet.append_row([score_entry["date"], score_entry["pt"], score_entry["raw"], score_entry["scaled"], score_entry["notes"]])
