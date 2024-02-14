import openpyxl

wb = openpyxl.Workbook()
sheet = wb["Sheet"]
sheet["A1"] = "Tal row"
sheet["B2"] = "Wide column"

# set the height and width:
sheet.row_dimensions[1].height = 70
sheet.column_dimensions["B"].width = 20
wb.save("./size/dimension.xlsx")
