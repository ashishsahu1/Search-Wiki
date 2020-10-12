from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

lst=[]
term = "tiger"
html = urlopen('https://en.wikipedia.org/wiki/{}'.format(term.replace(" ","")))
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
for i in images:
    lst.append(str(i['src']))

print(lst)
