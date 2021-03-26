import gspread
from oauth2client.service_account import ServiceAccountCredentials




# row = sheet.row_values(2)
# col = sheet.col_values(1)
# cell = sheet.cell(1,1).value



scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

my_creds = ServiceAccountCredentials.from_json_keyfile_name("creds/creds.json", scope)

client = gspread.authorize(my_creds)

sheet = client.open("Money Operations").sheet1


def insert_gsheet_refcard(opdata):
    insert_row = [opdata["DATE"], opdata["TIME"],
                  opdata["operation"], opdata["SUM"],
                  "-", opdata["source"],
                  opdata["dest"], opdata["Type"]]

    data = sheet.get_all_records()
    numOfrow = len(data) + 2
    sheet.insert_row(insert_row, numOfrow)

def insert_gsheet_outcame(opdata):
    insert_row = [opdata["DATE"], opdata["TIME"],
                  opdata["operation"],opdata["sum"],
                  opdata["category"],opdata["money_source"],
                  "-", opdata["Type"]]

    data = sheet.get_all_records()
    numOfrow = len(data) + 2
    sheet.insert_row(insert_row, numOfrow)


def insert_gsheet_salary(opdata):
    insert_row = [opdata["DATE"], opdata["TIME"],
                  opdata["operation"], opdata["sum"],
                  "-", "-",opdata["dest"],opdata["Type"]]

    data = sheet.get_all_records()
    numOfrow = len(data) + 2
    sheet.insert_row(insert_row, numOfrow)