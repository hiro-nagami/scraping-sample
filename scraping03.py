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

# マップ情報を取得
forecastMap = bsObj.find('div', id="forecastMap")

# 各地の天気情報を取得
points =  forecastMap.find_all(class_="point")

for p in points:
    # 地名
    name = p.find(class_="name").string
    # 天気
    weather = p.find(class_="forecast").find('img')['alt']
    # 最高気温
    high = p.find(class_="temp").find(class_="high").string
    # 最低気温
    low = p.find(class_="temp").find(class_="low").string
    # 降水確率
    precip = p.find(class_="precip").string

    print(name, weather, high, "/", low, precip)