# 第16章　处理CSV文件和JSON数据

## CSV和JSON简介

- CSV表示“Comma-Separated Values”（逗号分隔的值）。它是一种简化的电子表格，被保存为纯文本文件。Python的csv模块可以方便地处理CSV文件。

- JSON（JavaScript Object Notation）是一种将信息保存在纯文本文件中的格式。它以JavaScript源代码的形式呈现，但你不需要了解JavaScript编程语言就可以使用JSON文件。

## CSV文件操作

### 读取CSV文件

- 使用`csv.reader()`函数可以创建一个reader对象，这个对象允许你遍历CSV文件中的每一行。

```python
import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)
```

- 你也可以在一个for循环中使用reader对象，这样可以避免一次性将整个文件加载到内存中。

```python
import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
```

### 写入CSV文件

- 使用`csv.writer()`函数可以创建一个writer对象，这个对象可以将数据写入CSV文件。

```python
import csv

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputFile.close()
```

### 使用delimiter和lineterminator关键字参数

- 你可以使用`delimiter`和`lineterminator`关键字参数来改变你的文件中的分隔符和行终止字符。

```python
import csv

csvFile = open('example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvFile.close()
```

### 使用DictReader和DictWriter CSV对象

- 对于包含列标题行的CSV文件，通常使用`DictReader`和`DictWriter`对象，而不是使用reader和writer对象，因为这样会更方便。

```python
import csv

exampleFile = open('exampleWithHeader.csv')
exampleDictReader = csv.DictReader(exampleFile)
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
```

## JSON操作

### 读取JSON

- 使用`json.loads()`函数可以将包含JSON数据的字符串转换为Python的值。

```python
import json

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)
```

### 写入JSON

- 使用`json.dumps()`函数可以将一个Python值转换成JSON格式的数据字符串。

```python
import json

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)
```

## 整理成笔记

以下是合并后的完整表格：

| 函数/方法                             | 说明                                                  | 可选参数                                          |
| ------------------------------------- | ----------------------------------------------------- | ------------------------------------------------- |
| `csv.reader(fileObj)`                 | 返回一个reader对象，可以遍历CSV文件中的每一行         | `fileObj`: 文件对象                               |
| `csv.writer(fileObj)`                 | 返回一个writer对象，可以将数据写入CSV文件             | `fileObj`: 文件对象                               |
| `csv.DictReader(fileObj)`             | 返回一个DictReader对象，可以读取包含列标题行的CSV文件 | `fileObj`: 文件对象                               |
| `csv.DictWriter(fileObj, fieldnames)` | 返回一个DictWriter对象，可以写入包含列标题行的CSV文件 | `fileObj`: 文件对象<br>`fieldnames`: 列标题的列表 |
| `readerObj.line_num`                  | 返回当前读取的行号                                    | 无                                                |
| `writerObj.writerow(row)`             | 将一行数据写入CSV文件                                 | `row`: 一个列表，包含要写入的数据                 |
| `dictWriterObj.writeheader()`         | 将列标题写入CSV文件                                   | 无                                                |
| `dictWriterObj.writerow(rowDict)`     | 将一行数据写入CSV文件                                 | `rowDict`: 一个字典，包含要写入的数据             |
| `json.loads(jsonString)`              | 将包含JSON数据的字符串转换为Python的值                | `jsonString`: 包含JSON数据的字符串                |
| `json.dumps(pythonValue)`             | 将一个Python值转换成JSON格式的数据字符串              | `pythonValue`: 一个Python值                       |



## 项目：取得当前的天气数据

- 该程序需要完成以下任务：从命令行读取请求的位置，从OpenWeather官网下载JSON天气数据，将JSON数据字符串转换成Python的数据结构，输出今天和未来两天的天气。

```python
import json, requests, sys

# 从命令行读取请求的位置
location = ' '.join(sys.argv[1:])

# 从OpenWeather官网下载JSON天气数据
url ='https://api.op****data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()

# 将JSON数据字符串转换成Python的数据结构
weatherData = json.loads(response.text)

# 输出今天和未来两天的天气
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
```

## 项目：从CSV文件中删除标题行

- 该程序需要完成以下任务：找出当前工作目录中的所有CSV文件，读取每个文件的全部内容，跳过第一行，将内容写入一个新的CSV文件。

```python
import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# 遍历当前工作目录中的所有CSV文件
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    # 将内容写入新的CSV文件
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
```

## 项目：Excel到CSV的转换程序

- 该程序需要完成以下任务：循环遍历当前工作目录中的所有Excel文件，读取每个文件的全部内容，为每个工作表创建一个CSV文件。

```python
import openpyxl, csv, os

for excelFile in os.listdir('.'):
    # 跳过非xlsx文件，加载工作簿对象
    if not excelFile.endswith('.xlsx'):
        continue
    wb = openpyxl.load_workbook(excelFile)

    for sheetName in wb.get_sheet_names():
        # 循环遍历工作簿中的每个表
        sheet = wb.get_sheet_by_name(sheetName)

        # 创建CSV文件名
        csvFilename = excelFile[:-5] + '_' + sheetName + '.csv'
        csvFileObj = open(csvFilename, 'w', newline='')
        csvWriter = csv.writer(csvFileObj)

        # 循环遍历表中的每一行
        for rowNum in range(1, sheet.max_row + 1):
            rowData = []
            # 循环遍历行中的每个单元格
            for colNum in range(1, sheet.max_column + 1):
                rowData.append(sheet.cell(row=rowNum, column=colNum).value)
            # 将rowData写入CSV文件
            csvWriter.writerow(rowData)

        csvFileObj.close()
```