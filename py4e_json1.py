import json
data = '''
{
	"name" : "Tim",
	"phone" : {
		"type" : "intl",
		"number" : "+91 7891677153"
	},
	"email" : {
		"hide" : "yes"
	}
}'''

info = json.loads(data)
print("Name: ",info["name"])
print("Phone No. " , info["phone"]["number"])
print("Email-id: hidden :  " , info["email"]["hide"])