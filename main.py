import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "" # Enter your sheet id here
workbook = client.open_by_key(sheet_id)

values = [
    ["Name", "Price", "Quantity"],
    ["CricketBat", 2999.00, 1],
    ["Jarcy", 399.00, 4],
    ["Ball", 500.00, 3],
]

worksheet_list = map(lambda x: x.title, workbook.worksheets())
new_worksheet_name = "Values"

if new_worksheet_name in worksheet_list:
    sheet = workbook.worksheet(new_worksheet_name)
else:
    sheet = workbook.add_worksheet(new_worksheet_name, rows=10, cols=10)

sheet.clear()

sheet.update(f"A1:C{len(values)}", values)

sheet.update_cell(len(values) + 1, 2, "=sum(B2:B4)")
sheet.update_cell(len(values) + 1, 3, "=sum(C2:C4)")

sheet.format("A1:C1", {"textFormat": {"bold": True}})