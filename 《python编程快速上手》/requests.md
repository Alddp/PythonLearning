# 用 requests 模块从 Web 下载文件

## 安装 requests 模块

在命令行中执行以下命令安装 requests 模块：

```bash
pip install --user requests
```

## 导入 requests 模块

导入 requests 模块：

```python
import requests
```

## 使用 requests.get() 函数下载网页

```python
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
```

检查请求是否成功：

```python
res.status_code == requests.codes.ok  # 如果为 True，则表示请求成功
```

获取页面内容的长度：

```python
len(res.text)
```

显示部分页面内容：

```python
print(res.text[:250])
```

## 检查错误

使用 raise_for_status() 方法检查是否有错误：

```python
res.raise_for_status()
```

## 将下载的文件保存到硬盘

```python
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
```

以上是使用 requests 模块从 Web 下载文件并保存到硬盘的完整过程。