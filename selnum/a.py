import requests

res = requests.get("https://books.toscrape.com/?")

with open("a.txt", "wb") as f:
    for item in res.iter_content(100000):
        f.write(item)
