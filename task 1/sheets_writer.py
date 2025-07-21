import gspread
from oauth2client.service_account import ServiceAccountCredentials
import config

def store_in_sheets(data):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        config.GOOGLE_SHEETS_CREDENTIALS, scope
    )
    client = gspread.authorize(creds)

    # Open the precreated sheet
    sheet = client.open(config.GOOGLE_SHEET_NAME).sheet1

    # Add headers only if sheet is empty
    if not sheet.get_all_values():
        sheet.append_row(["Platform", "Title", "URL", "Engagement"])

    for row in data:
        sheet.append_row([row["platform"], row["title"], row["url"], row["engagement"]])
