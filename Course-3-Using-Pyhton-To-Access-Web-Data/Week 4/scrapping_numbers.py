#Scraping Numbers from HTML using BeautifulSoup 

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter -")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
tags = soup('span')
for tag in tags:
    number = int(tag.contents[0])
    sum += number
print(sum)