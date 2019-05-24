import urllib.parse , urllib.request, urllib.error
from twurl import augment
import ssl

print("***Calling Twitter***")
dictionary = {"screen_name": "drchuck", "count" : "2"}
url = augment("https://api.twitter.com/1.1/statuses/user_timeline.json",dictionary)
print(url)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url,context= ctx)
data = connection.read()
print(data)

headers = dict(connection.getheaders())
print(headers) 