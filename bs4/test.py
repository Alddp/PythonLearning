import requests, bs4, sys


res = requests.get("https://books.toscrape.com/")
try:
    res.raise_for_status()
except Exception as e:
    print(e)
    sys.exit()

with open("school.txt", "wb") as f:
    for trunk in res.iter_content(100000):
        f.write(trunk)
# default > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child(1) > article > h3 > a
# #default > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child(2) > article > h3 > a
soup = bs4.BeautifulSoup(res.text, "lxml")
elems = soup.select(
    "#default > div > div > div > div > section > div:nth-child(2) > ol > li > article > h3 > a"
)
for i in elems:
    # print(i.get('href'))
    # print(i.get('title'))
    print(i.name)
