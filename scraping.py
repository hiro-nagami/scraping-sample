from bs4 import BeautifulSoup
from urllib.request import urlopen

try:
    html = urlopen("http://pythonscraping.comi/blog/second-edition-changes")
    bsObj = BeautifulSoup(html, "html.parser")

    print(bsObj.h1)
    print(bsObj.h2)
except HTTPError as e:
    print (e)
except URLError as e:
    print ("The server could not found.")
else:
    print ("It worked.")



