from openpyxl.styles import Font
import openpyxl

wb = openpyxl.Workbook()
sheet = wb["Sheet"]


italic24Font = Font(size=24, italic=True)  # Create a font.
sheet["A1"].font = italic24Font  # Apply the font to A1.
sheet["A1"] = "Hello, world!"

fontObj1 = Font(name="Times New Roman", bold=True)
sheet["A1"].font = fontObj1
sheet["A1"] = "Bold Times New Roman"
fontObj2 = Font(size=24, italic=True)
sheet["B3"].font = fontObj2
sheet["B3"] = "24 pt Italic"
wb.save("styles.xlsx")
