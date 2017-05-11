from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
link = "https://pythonprogramming.net/parsememcparseface"
try:
#    open_url = urlopen("https://ca.indeed.com/jobs?q=research+analyst&l=Ontario")
    open_url = urlopen(link)

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


# to get special URL

nav= soup.nav # just get information within nav :)
print(nav)

for url in nav.find_all('a'):
    print(url.get('href'))

body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)

print("================== NEW COMMAND STARTING =================")

for div in soup.find_all('div', class_ = 'body'):
    print(div.text)


# to parse table <tr>

table = soup.table
#print (table)
# OR (both are same)
table = soup.find('table')
#print(table)

print("================== NEW COMMAND STARTING =================")
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)


import pandas as pd

dfs = pd.read_html(link, header=0)

for df in dfs:
    print(df)



# reading sidemaps
print("================== SIDEMAPS STARTING =================")

sitemap = "https://pythonprogramming.net/sitemap.xml"
open_url = urlopen(sitemap)
soup = BeautifulSoup(open_url.read(), "xml")

for url in soup.find_all('loc'):
    print(url.text)


