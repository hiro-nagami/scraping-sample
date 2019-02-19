from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

class DayWeather:
    def __init__(self, name, weather, high, low, precip):
        self.name = name
        self.weather = weather
        self.high = high
        self.low = low
        self.precip = precip

def getHtml(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    }

    session = requests.Session()
    return session.get(url, headers=headers)

def getRelatedLinks(baseUrl):
    l = [baseUrl]
    try:
        response = getHtml(baseUrl)
        bsObj = BeautifulSoup(response.text, "html.parser")
        cal = bsObj.find('ul', id="navCal")
        days = cal.find_all('li')

        for day in days:
            link = day.a
            # if link:
            if link is not None:
                url = urljoin(baseUrl, link.get("href"))
                l.append(url)
        return l
    except TypeError as e:
        print('catch TypeError:', e)
        pass

def printDay(response):
    try:
        bsObj = BeautifulSoup(response.text, "html.parser")
        cal = bsObj.find('ul', id="navCal")
        day = cal.find('span', class_="current")
        print()
        print(day.text)
    except TypeError as e:
        print('catch TypeError:', e)
        pass

def findForecastMap(response):
    try:
        bsObj = BeautifulSoup(response.text, "html.parser")
        return bsObj.find('div', id="forecastMap")
    except TypeError as e:
        print('catch TypeError:', e)
        pass

def getWeathersFromForecastMap(map):
    try: 
        weathers = []
        points =  map.find_all(class_="point")

        for p in points:
            try:
                name = p.find(class_="name").string
                weather = p.find(class_="forecast").find('img')['alt']
                high = p.find(class_="temp").find(class_="high").string
                low = p.find(class_="temp").find(class_="low").string
                precip = p.find(class_="precip").string

                weathers.append(DayWeather(name, weather, high, low, precip))
            
            except TypeError as e:
                print('catch TypeError:', e)
                pass
        return weathers
    except TypeError as e:
        print('catch TypeError:', e)
        pass

url = "https://weather.yahoo.co.jp/weather"
relatedLinks = getRelatedLinks(url)

for link in relatedLinks:
    response = getHtml(link)
    printDay(response)
    forecastMap = findForecastMap(response)
    weathers = getWeathersFromForecastMap(forecastMap)

    for w in weathers:
        print(w.name, w.weather, w.high, "/", w.low, w.precip)

