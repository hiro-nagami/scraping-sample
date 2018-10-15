from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

try:
    html = urlopen("https://weather.yahoo.co.jp/weather")
    bsObj = BeautifulSoup(html, "html.parser")

    print("[h1] " + bsObj.h1.text)
    print("[h2] " + bsObj.h2.text)
    # print(bsObj.html)
except HTTPError as e:
    print (e)
except URLError as e:
    print ("The server could not found.")
else:
    print ("It worked.")



