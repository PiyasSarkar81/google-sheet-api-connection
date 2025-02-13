# ☁️ Connecting Google Sheets with Python Using Google Cloud Credentials

## Overview
This guide explains how to use Python to interact with Google Sheets using the `gspread` library and Google Cloud credentials. You will learn how to authenticate, access a Google Sheet, write data, apply formulas, and format cells.

## Prerequisites
Before running the script, ensure you have:
- A Google Cloud project with the Google Sheets API enabled.
- A service account with a JSON key file.
- Installed the required Python libraries (`gspread`, `google-auth`).

## Setup Instructions

### 1. Enable Google Sheets API
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Navigate to **APIs & Services > Library** and enable **Google Sheets API**.
4. Go to **APIs & Services > Credentials**, create a new **Service Account**, and download the JSON key file.
5. Share your Google Sheet with the service account email (found in the JSON file) with **Editor** access.

### 2. Install Required Libraries
Run the following command to install dependencies:
```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib gspread
```

### 3. Run the Script
Execute the script using:
```bash
python main.py
```

## Notes
- Ensure that `credentials.json` is in the same directory as the script.
- Replace `sheet_id` with your actual Google Sheet ID.
- You can modify the script to add more complex operations like reading, updating, or deleting rows.

## References
- [Google Sheets API Documentation](https://developers.google.com/sheets/api)
- [gspread Documentation](https://docs.gspread.org/)

Happy coding! 🚀

