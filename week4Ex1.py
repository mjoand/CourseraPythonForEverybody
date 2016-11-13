import urllib
import re
from BeautifulSoup import *

url ="http://python-data.dr-chuck.net/comments_209844.html"
html = urllib.urlopen(url).read()

soup=BeautifulSoup(html)
tags=soup('span')
soma=0

for tag in tags:
  soma=soma+int(tag.contents[0])
  
print(soma)

 




