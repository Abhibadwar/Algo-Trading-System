import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Function to log a row of data to Google Sheets
def log_to_google_sheets(row_data, sheet_name='AlgoTradingLog'):
    try:
        # Define Google API scopes
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        
        # Load credentials from your JSON key file
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        
        # Authorize client
        client = gspread.authorize(creds)
        
        # Open Google Sheet by name
        sheet = client.open(sheet_name).sheet1  # or use .worksheet('Sheet1') if needed
        
        # Optional: prepend current datetime
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        row_data = [timestamp] + row_data

        # Append data
        sheet.append_row(row_data)
        print("✅ Logged to Google Sheets successfully.")

    except Exception as e:
        print("❌ Failed to log to Google Sheets:", e)
