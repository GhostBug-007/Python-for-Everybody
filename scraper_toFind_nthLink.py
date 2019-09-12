#Web Scraper to find the nth element on a page and visit it for x times

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl,re
#ssl certificates for https *\"comments\">
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode

anchor=[]
mainList = []
url = input("Enter -")
count=int(input("Enter count: "))
position =int(input("Enter position: "))
for i in range(count):
	html = urllib.request.urlopen(url,context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags=soup("a")
	for tag in tags:
		x = str(tag.get("href"))
		if x.startswith('http'):
			anchor.append(x)
	mainList.append(anchor[position-1])
	print(anchor[position-1])
	url=anchor[position-1]
	anchor=[]