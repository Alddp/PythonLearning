from bs4 import BeautifulSoup

html = '<a target="_blank" href="https://pypi.com.cn/" h="ID=SERP,5238.2" style=""><strong>PyPI</strong>中文网</a>'

# 创建 Beautiful Soup 对象
soup = BeautifulSoup(html, "lxml")

# 提取链接文本和 URL
soup.a.text  # 提取链接文本
soup.a["href"]  # 提取链接 URL
soup.select("a[target]")
soup.select("a[target=_blank]")
