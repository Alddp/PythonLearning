# 用bs4模块解析HTML

## 简介

Beautiful Soup 是一个模块，用于从HTML页面中提取信息。它的名字是bs4，表示Beautiful Soup第4版。在Python中，我们通过`pip install beautifulsoup4`进行安装，然后通过`import bs4`来导入使用。

在HTML文件中，我们可以看到许多不同的标签和属性。对于复杂的网站，这会变得令人困惑。但是，使用Beautiful Soup 可以让处理HTML变得容易很多。

## 从HTML创建一个BeautifulSoup对象

`bs4.BeautifulSoup()` 函数需要一个字符串，其中包含将要解析的HTML。它返回一个BeautifulSoup 对象。

```python
import requests, bs4

res = requests.get('https://nosta')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)
```

以上代码从No Starch出版社网站下载主页，然后将响应结果的text 属性传递给`bs4.BeautifulSoup()`。返回的BeautifulSoup 对象保存在变量`noStarchSoup` 中。

我们也可以向`bs4.BeautifulSoup()` 传递一个File 对象，以及第二个参数，告诉Beautiful Soup 使用哪个解析器来分析HTML。

```python
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
type(exampleSoup)
```

这里使用的'html.parser' 解析器是 Python 自带的。但是，如果你安装了第三方`lxml` 模块，你就可以使用更快的'lxml' 解析器。

## 用select()方法寻找元素

我们可以调用一个BeautifulSoup 对象的`select()` 方法，传入一个字符串作为CSS“选择器”，就可以取得一个Web页面元素。选择器就像正则表达式：它们指定了要寻找的模式，在这个例子中，是在HTML页面中寻找，而不是在普通的文本字符串中寻找。

以下是一份选择器的简单介绍。

| 传递给select()方法的选择器          | 将匹配……                                                 |
| ----------------------------------- | -------------------------------------------------------- |
| soup.select('div')                  | 所有名为<div> 的元素                                     |
| soup.select('#author')              | 带有id属性为author的元素                                 |
| soup.select('.notice')              | 所有使用CSS class属性名为notice的元素                    |
| soup.select('div span')             | 所有在<div> 元素之内的<span> 元素                        |
| soup.select('div > span')           | 所有直接在<div> 元素之内的<span> 元素，中间没有其他元素  |
| soup.select('input[name]')          | 所有名为<input> ，并有一个name 属性，其值无所谓的元素    |
| soup.select('input[type="button"]') | 所有名为<input> ，并有一个type 属性，其值为button 的元素 |

```python
import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
type(elems)
len(elems)
type(elems[0])
str(elems[0])
elems[0].getText()
elems[0].attrs
```

以上代码将带有id="author" 的元素从示例HTML中找出来。

```python
pElems = exampleSoup.select('p')
str(pElems[0])
pElems[0].getText()
str(pElems[1])
pElems[1].getText()
str(pElems[2])
pElems[2].getText()
```

以上代码则是从BeautifulSoup 对象中找出<p> 元素。

## 通过元素的属性获取数据

Tag 对象的`get()` 方法让我们很容易从元素中获取属性值。向该方法传入一个属性名称的字符串，它将返回该属性的值。

```python
import bs4

soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]
str(spanElem)
spanElem.get('id')
spanElem.get('some_nonexistent_addr') == None
spanElem.attrs
```

以上代码使用`select()` 来寻找所有<span> 元素，然后将第一个匹配的元素保存在`spanElem` 中。将属性名'id' 传递给`get()` 以返回该属性的值'author' 。