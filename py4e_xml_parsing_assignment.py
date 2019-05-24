import xml.etree.ElementTree as ET 
import urllib.parse, urllib.error, urllib.request
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode

url=input("Enter- ")
openUrl=urllib.request.urlopen(url,context=ctx).read()
file = ET.fromstring(openUrl)
lst = file.findall(".//count")
sumTotal=0
for item in lst:
	sumTotal+= int(item.text)
print(sumTotal)

