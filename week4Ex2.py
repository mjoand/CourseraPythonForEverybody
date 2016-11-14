# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url =raw_input('Enter first link - ')

###use link bellow:
### http://python-data.dr-chuck.net/known_by_Temi.html

pos=int(raw_input('Position:'))-1

times=int(raw_input('How many times?:'))

print url

for i in range(times):
 html = urllib.urlopen(url).read()
 soup = BeautifulSoup(html)
 url=soup('a')[pos].get('href', None)
 print url
 
 


