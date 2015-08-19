from urllib.request import urlopen

from bs4 import BeautifulSoup

__author__ = 'ye'

# html=urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
try:
    html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html_mock")
    bsObj = BeautifulSoup(html.read())
    print(bsObj.h1)
except Exception as error:
    print("hehe : ",error)
    raise error
else:
    print('from else')
finally:
    print("form finally")
