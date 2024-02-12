import requests, bs4

res = requests.get("https://books.toscrape.com/")
res.raise_for_status()
with open("school.txt", "wb") as f:
    for trunk in res.iter_content():
        f.write(trunk)
douban = bs4.BeautifulSoup(res.text, "lxml")
elems = douban.select("div")
douban.img
