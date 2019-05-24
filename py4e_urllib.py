import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl,re
#ssl certificates for https *\"comments\">
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode

url = input("Enter -")
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
sumx=0
tags = soup("tr")
for tag in tags: 
	x=str(tag.contents[1])
	x=re.findall("\"comments\">(\S+)</s",x)
	for value in x:
		sumx+=int(value)
	# sumx+=int(x[0])
print(sumx)
