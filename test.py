from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

term = "evans"
html = urlopen('https://en.wikipedia.org/wiki/{}'.format(term.replace(" ","")))
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
print(images[0]['src']+'\n')

