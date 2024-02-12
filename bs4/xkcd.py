#!蟒蛇3
# downloadXkcd.py - 下载每一部 XKCD 漫画。
##comic > img
import requests, os
from bs4 import BeautifulSoup


def download_xkcd(start_page: int, end_page: int):
    os.makedirs("xkcd", exist_ok=True)  # 将漫画存储在 ./xkcd 中

    for page in range(start_page, end_page + 1):
        url = "https://xkcd.com/" + str(page)
        # TODO：下载页面。
        print("Downloading...")
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")

        # TODO：找到漫画图片的 URL。
        comic_element = soup.select("#comic > img")
        if comic_element == []:
            print("Could not find image.")
        else:
            comic_url = "https:" + comic_element[0].get("src")

        # TODO：下载图片。
        # 如果图片存在,跳过
        image_path = os.path.join("xkcd", os.path.basename(comic_url))
        if os.path.exists(image_path):
            print("already exists!")
            continue
        print("Downloading   %s" % (comic_url))
        res = requests.get(comic_url)
        # 下载失败处理
        try:
            res.raise_for_status()
        except Exception as e:
            print("something wrong...", e)
            continue
        # TODO：将图片保存到 ./xkcd。

        with open(os.path.join("xkcd", os.path.basename(comic_url)), "wb") as f:
            for trunk in res.iter_content(100000):
                f.write(trunk)
        print("Done.")
    print("Finish!")


if __name__ == "__main__":
    start = int(input("开始页数:"))
    end = int(input("结束页数:"))
    download_xkcd(start_page=start, end_page=end)
