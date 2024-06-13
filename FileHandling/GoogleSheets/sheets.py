import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Adding drive scope to get file from drive
scopes=[
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds=ServiceAccountCredentials.from_json_keyfile_name('secrets_key.json',scopes=scopes)

client=gspread.authorize(creds)

def reading_sheet(workbook_name):

    #Opening Workbook
    workbook=client.open(workbook_name)

    sheet=workbook.sheet1

    data=sheet.get_all_values()
    #print(data[0][1])
    for d in data:
        print(d)
    print(data)

    #Printing Cell Value
    print(sheet.acell('A2').value)


def writing_sheet(workbook_name):
    workbook = client.open(workbook_name)

    sheet = workbook.sheet1

    #Update a cell value
    sheet.update_acell('A2',"Usman")

    #Append and write data to sheet

    sheet.append_row(['NewlyAdded', '23', '63', 'A'])



writing_sheet('MySheet')

reading_sheet('MySheet')
