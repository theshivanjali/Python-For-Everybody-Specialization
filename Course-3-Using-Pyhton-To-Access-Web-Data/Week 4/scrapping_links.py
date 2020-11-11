import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter URL: ")
count = int(input("Enter Count: "))
position = int(input("Enter Position: "))

print("Retrieving: ",url)

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    nexturl = tags[position-1].get("href", None)
    print("Retrieving: ",nexturl)
    url = nexturl