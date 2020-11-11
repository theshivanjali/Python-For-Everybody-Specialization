import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    info = json.loads(data)
except:
    info = None

sum = 0

# print(json.dumps(info, indent=4))

for item in info['comments']:
    sum += int(item['count'])

print(sum)

