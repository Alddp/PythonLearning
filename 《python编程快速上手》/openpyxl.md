# 处理Excel电子表格

## Excel文档基础

- Excel电子表格文档称为一个“工作簿”，保存在扩展名为.xlsx的文件中。每个工作簿可以包含多个“表”（也称为“工作表”）。
- 用户当前查看的表（或关闭Excel前最后查看的表）称为“活动表”。
- 每个表都有一些“列”（地址是从A开始的字母）和一些“行”（地址是从1开始的数字）。处于特定行和列的方格称为“单元格”。每个单元格包含一个数字或文本值，或者是空白。单元格形成的网格和数据构成了表。

## 安装openpyxl模块

- Python没有自带openpyxl，所以必须安装。模块的名称是openpyxl。

```python
pip install openpyxl
```

## 读取Excel文档

- 使用openpyxl模块可以打开一个Excel文件，返回一个Workbook对象。
- Workbook对象的sheetnames属性可以返回一个包含所有表名的列表。
- 可以通过索引或工作表的名字来获取一个Worksheet对象。
- Cell对象有一个value属性，它包含这个单元格中保存的值。

```python
import openpyxl

wb = openpyxl.load_workbook('example.xlsx')  # 打开一个Excel文件
sheet = wb['Sheet1']  # 获取一个工作表
cell = sheet['A1']  # 获取一个单元格
print(cell.value)  # 打印单元格的值
```

## 写入Excel文档

- 可以通过赋值来改变单元格的值。
- Workbook对象的save方法可以将改变保存到电子表格文件中。

```python
import openpyxl

wb = openpyxl.Workbook()  # 创建一个新的工作簿
sheet = wb.active  # 获取活动工作表
sheet['A1'] = 'Hello, world!'  # 改变单元格的值
wb.save('example.xlsx')  # 保存工作簿
```

## 创建和删除工作表

- Workbook对象的create_sheet方法可以创建一个新的工作表。
- 可以通过del操作符从工作簿中删除一个工作表。

```python
import openpyxl

wb = openpyxl.Workbook()  # 创建一个新的工作簿
wb.create_sheet(index=0, title='First Sheet')  # 创建一个新的工作表
del wb['Sheet']  # 删除一个工作表
```

## 设置单元格的字体风格

- 可以通过设置Cell对象的font属性来改变单元格的字体风格。

```python
from openpyxl.styles import Font

fontObj = Font(name='Times New Roman', bold=True)  # 创建一个字体对象
sheet['A1'].font = fontObj  # 设置单元格的字体
sheet['A1'] = 'Bold Times New Roman'  # 改变单元格的值
```

## 公式

- 可以将公式作为单元格的值进行设置。

```python
sheet['B9'] = '=SUM(B1:B8)'  # 设置公式
```

## 调整行和列

- Worksheet对象的row_dimensions和column_dimensions属性可以用于控制行高和列宽。
- Worksheet对象的merge_cells方法可以将一个矩形区域中的单元格合并为一个单元格。

- Worksheet对象的freeze_panes属性可以**冻结窗格。**

```python
sheet.row_dimensions[1].height = 70  # 设置行高
sheet.column_dimensions['B'].width = 20  # 设置列宽
sheet.merge_cells('A1:D3')  # 合并单元格
sheet.freeze_panes = 'A2'  # 冻结窗格
```

## 图表

- openpyxl模块支持创建条形图、折线图、散点图和饼图。

```python
from openpyxl.chart import Reference, Series, BarChart

values = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)  # 创建一个Reference对象
series = Series(values, title='First series')  # 创建一个Series对象
chart = BarChart()  # 创建一个Chart对象
chart.append(series)  # 将Series对象添加到Chart对象
sheet.add_chart(chart, 'C5')  # 将Chart对象添加到Worksheet对象
```

## 整理成笔记

以下是合并后的完整表格：

| 函数/方法                                                    | 说明                                     | 可选参数                                                     |
| ------------------------------------------------------------ | ---------------------------------------- | ------------------------------------------------------------ |
| `openpyxl.load_workbook(filename, read_only, keep_vba, data_only, keep_links)` | 打开一个Excel文件，返回一个Workbook对象  | `filename`: 文件名<br>`read_only`: 只读模式<br>`keep_vba`: 保留vba<br>`data_only`: 只读数据<br>`keep_links`: 保留链接 |
| `openpyxl.Workbook()`                                        | 创建一个新的工作簿                       | 无                                                           |
| `Workbook.sheetnames`                                        | 返回一个包含所有表名的列表               | 无                                                           |
| `Workbook.active`                                            | 返回工作簿的活动工作表的Worksheet对象    | 无                                                           |
| `Workbook.create_sheet(title, index)`                        | 创建一个新的工作表                       | `title`: 工作表的名字<br>`index`: 工作表的位置               |
| `Workbook.save(filename)`                                    | 将改变保存到电子表格文件中               | `filename`: 文件名                                           |
| `Worksheet['cell']`                                          | 获取一个单元格                           | `cell`: 单元格坐标，如'A1'                                   |
| `Cell.value`                                                 | 返回或设置单元格的值                     | 无                                                           |
| `Cell.row`                                                   | 返回单元格的行号                         | 无                                                           |
| `Cell.column`                                                | 返回单元格的列号                         | 无                                                           |
| `Cell.coordinate`                                            | 返回单元格的坐标                         | 无                                                           |
| `Worksheet.max_row`                                          | 返回表中的最大行数                       | 无                                                           |
| `Worksheet.max_column`                                       | 返回表中的最大列数                       | 无                                                           |
| `openpyxl.utils.column_index_from_string(col)`               | 返回列的整数索引                         | `col`: 列的字母，如'M'                                       |
| `openpyxl.utils.get_column_letter(idx)`                      | 返回列的字符串名称                       | `idx`: 列的整数索引，如14                                    |
| `Worksheet.row_dimensions`                                   | 返回一个字典，用于控制行高               | 无                                                           |
| `Worksheet.column_dimensions`                                | 返回一个字典，用于控制列宽               | 无                                                           |
| `Worksheet.merge_cells(range_string)`                        | 将一个矩形区域中的单元格合并为一个单元格 | `range_string`: 单元格的范围，如'A1:D3'                      |
| `Worksheet.unmerge_cells(range_string)`                      | 将一个矩形区域中的单元格拆分为多个单元格 | `range_string`: 单元格的范围，如'A1:D3'                      |
| `Worksheet.freeze_panes`                                     | 冻结窗格                                 | 无                                                           |
| `openpyxl.styles.Font(name, size, bold, italic)`             | 创建一个字体对象                         | `name`: 字体名称，如'Times New Roman'<br>`size`: 字体大小<br>`bold`: 是否加粗<br>`italic`: 是否斜体 |
| `openpyxl.chart.Reference(worksheet, min_col, min_row, max_col, max_row)` | 创建一个Reference对象                    | `worksheet`: 包含图表数据的Worksheet对象<br>`min_col`: 矩形选择区域的左上角单元格的列<br>`min_row`: 矩形选择区域的左上角单元格的行<br>`max_col`: 矩形选择区域的右下角单元格的列<br>`max_row`: 矩形选择区域的右下角单元格的行 |
| `openpyxl.chart.Series(values, title)`                       | 创建一个Series对象                       | `values`: 一个Reference对象<br>`title`: 系列的标题           |
| `openpyxl.chart.BarChart()`                                  | 创建一个条形图                           | 无                                                           |
| `Chart.append(series)`                                       | 将Series对象添加到Chart对象              | `series`: 一个Series对象                                     |
| `Worksheet.add_chart(chart, cell)`                           | 将Chart对象添加到Worksheet对象           | `chart`: 一个Chart对象<br>`cell`: 单元格坐标，如'C5'         |

## 项目实践

1. **乘法表**

```python
import openpyxl
from openpyxl.utils import get_column_letter

def create_multiplication_table(n):
    wb = openpyxl.Workbook()
    sheet = wb.active

    for i in range(1, n+2):
        for j in range(1, n+2):
            if i == 1 and j == 1:
                continue
            elif i == 1:
                sheet[get_column_letter(j)+str(i)] = j-1
            elif j == 1:
                sheet[get_column_letter(j)+str(i)] = i-1
            else:
                sheet[get_column_letter(j)+str(i)] = (i-1) * (j-1)

    wb.save('multiplication_table.xlsx')

create_multiplication_table(6)
```

2. **空行插入程序**

```python
import openpyxl

def insert_blank_rows(file, row, num):
    wb = openpyxl.load_workbook(file)
    sheet = wb.active

    for i in range(row, sheet.max_row+1)[::-1]:
        for j in range(1, sheet.max_column+1):
            cell