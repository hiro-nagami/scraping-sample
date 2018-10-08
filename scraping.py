from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://pythonscraping.com/blog/second-edition-changes")
bsObj = BeautifulSoup(html, "html.parser")

print(bsObj.h1)
print(bsObj.h2)

