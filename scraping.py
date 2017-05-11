from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
try:
    open_url = urlopen("https://ca.indeed.com/jobs?q=research+analyst&l=Ontario")
    soup = BeautifulSoup(open_url.read(), "lxml")
except HTTPError as he:
    print(he)
    exit()
except AttributeError as ae:
    print(ae)
    exit()

print(soup.title)

