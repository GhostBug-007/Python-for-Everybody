import urllib.parse, urllib.error, urllib.request
import json
url = input("Enter- ")
data = urllib.request.urlopen(url).read()

info = json.loads(data)
# print(info["comments"])
sum=0
for dictionary in info["comments"]:
		sum += dictionary["count"]
			# print(dictionary["count"],sum)
print(sum)

# print(info)