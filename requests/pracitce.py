import requests
from bs4 import BeautifulSoup


def check_links(url):
    # 下载页面
    response = requests.get(url)
    response.raise_for_status()  # 如果请求失败，这会抛出一个异常

    # 解析页面并找到所有的链接
    soup = BeautifulSoup(response.text, "lxml")
    links = [a["href"] for a in soup.find_all("a", href=True)]

    # 检查每个链接的状态码
    for link in links:
        try:
            response = requests.head(link, allow_redirects=True)
            if response.status_code == 404:
                print(f"Bad link: {link}")
        except requests.exceptions.RequestException:
            print(f"Invalid link: {link}")


# 检查一个网页的链接
check_links("https://zh.wikipedia.org/")
