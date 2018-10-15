from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
}
url = "https://weather.yahoo.co.jp/weather"

session = requests.Session()

req = session.get(url, headers=headers)
bsObj = BeautifulSoup(req.text, "html.parser")

print("[h1] " + bsObj.h1.text)
print("[h2] " + bsObj.h2.text)
# print(bsObj.html)

print ("It worked.")
