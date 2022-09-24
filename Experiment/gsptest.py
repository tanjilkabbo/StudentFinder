import gspread

gc = gspread.service_account('../studentfindergspreed-aa5ba05c0365.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("StudentFinder").sheet1

print(wks)