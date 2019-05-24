import urllib.parse, urllib.error , urllib.request
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True :
	address = input("Enter Location: ")
	if len(address) < 1 : break

	parms = dict()
	parms["address"]  = address 
	parms["key"] = api_key 
	url = serviceurl + urllib.parse.urlencode(parms)

	print("Retrieving" , url)
	data = urllib.request.urlopen(url, context = ctx)
	info = data.read().decode()
	print("Retrieved", len(info), "character")

	try:
		js =json.loads(info)
	except:
		js = None

	if not js or "status" not in js or js["status"] != "OK" :
		print("-----Failure To Retrieve Data-----")

	# print(json.dumps(js,indent = 2))
	# print("\nplace_id : ", js["results"]["place_id"])
	for item in js["results"]:
		print("Place id ", item["place_id"])


