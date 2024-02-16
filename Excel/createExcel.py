import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet.title = "test"
wb.save("cerate_excel.xlsx")
