from urllib.request import urlopen
from bs4 import BeautifulSoup
open_url = urlopen("https://ca.indeed.com/jobs?q=research+analyst&l=Ontario")
soup = BeautifulSoup(open_url.read(), "lxml")
print(soup.title)
