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

def findForecastMap(response):
    try:
        bsObj = BeautifulSoup(response.text, "html.parser")
        return bsObj.find('div', id="forecastMap")
    except:
        print("cannot find forecastMap")
        pass

def getRelatedLinks(response):
    try:
        bsObj = BeautifulSoup(response.text, "html.parser")
        cal = bsObj.find('ul', id="navCal")
        days = cal.find_all('li')

        for day in days:
            print(day.em.string)

            link = day.a
            # if link:
            print(urljoin("", link.get("href")))
    except:
        print("cannot find navCal")
        pass

def getWeathersFromForecastMap(map):
    try: 
        weathers = []
        points =  map.find_all(class_="point")

        for p in points:
            try:
                name = p.find(class_="name").string
                weather = p.find(class_="forecast").span.string
                high = p.find(class_="temp").find(class_="high").string
                low = p.find(class_="temp").find(class_="low").string
                precip = p.find(class_="precip").string

                weathers.append(DayWeather(name, weather, high, low, precip))
            
            except:
                print("cannot find weather")
                pass
        return weathers
    except:
        print("cannot find point")
        pass

url = "https://weather.yahoo.co.jp/weather"
response = getHtml(url)
getRelatedLinks(response)
forecastMap = findForecastMap(response)
weathers = getWeathersFromForecastMap(forecastMap)

for w in weathers:
    print(w.name, w.weather, w.high, "/", w.low, w.precip)

