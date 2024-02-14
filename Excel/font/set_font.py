from openpyxl.styles import Font
import openpyxl

wb = openpyxl.Workbook()
sheet = wb["Sheet"]


italic24Font = Font(size=24, italic=True)  # Create a font.
sheet["A1"].font = italic24Font  # Apply the font to A1.
sheet["A1"] = "Hello, world!"
wb.save("./font/styles.xlsx")
