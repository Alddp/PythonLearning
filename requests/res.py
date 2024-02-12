import requests

res = requests.get("https://cn.bing.com/search?q=pypi")
with open("pypi.txt", "wb") as f:
    number = 0
    for chunk in res.iter_content():
        number += f.write(chunk)
