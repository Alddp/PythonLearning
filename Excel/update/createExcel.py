import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet.title = "spam"
sheet["A1"] = "Hello world"
wb.save("cerate_excel.xlsx")
