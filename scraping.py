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

# Choose whaterver you are interested into
print(soup.title)

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.text)
print(soup.p)

print(soup.find_all('p')) # good for news websites

for paragraph in soup.find_all('p'):
    print(paragraph.string) # if no child tag:
    print(paragraph.text) # most cases

print(soup.get_text())

for url in soup.find_all('a'):
    print(url.get('href'))
