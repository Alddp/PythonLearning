# python3
# Opens several search results.

import requests, webbrowser, bs4, sys

print("Searching...")
res = requests.get("https://cn.bing.com/search?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, "lxml")

# TODO: Open a browser tab for each result
link_elements = soup.select("a[target=_blank]")
num_open = min(5, len(link_elements))

for i in range(num_open):
    url_to_open = link_elements[i].get("href")
    print("Opening", url_to_open)
    webbrowser.open(url_to_open)
