from openpyxl.chart import Reference, Series, BarChart
import openpyxl

wb = openpyxl.Workbook()
sheet = wb["Sheet"]

values = Reference(
    sheet, min_col=1, min_row=1, max_col=1, max_row=10
)  # 创建一个Reference对象

series = Series(values, title="First series")  # 创建一个Series对象
chart = BarChart()  # 创建一个Chart对象
chart.append(series)  # 将Series对象添加到Chart对象
sheet.add_chart(chart, "C5")  # 将Chart对象添加到Worksheet对象

wb.save("./chart/set_chart.xlsx")
