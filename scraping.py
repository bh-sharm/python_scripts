form urllib.request inport urlopen
from bs4 import BeautifulSoup
open_url = urlopen("https://ca.indeed.com/jobs?q=research+analyst&l=Ontario")
soup = BeautifulSoup(openurl.read(), "lxml")
print(soup.title)
