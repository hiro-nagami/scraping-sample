from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

try:
    html = urlopen("http://pythonscraping.com/blog/second-edition-changes")
    bsObj = BeautifulSoup(html, "html.parser")

    print(bsObj.h1.text)
    print(bsObj.h2.text)
except HTTPError as e:
    print (e)
except URLError as e:
    print ("The server could not found.")
else:
    print ("It worked.")



