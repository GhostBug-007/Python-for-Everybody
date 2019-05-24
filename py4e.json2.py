import json
inputData= '''
[
	{
		"id" : "001",
		"x" : "2",
		"name" : "Lorry"
	},
	{
		"id" : "002",
		"x" : "4",
		"name" : "Harry"
	}
]'''

finalData = json.loads(inputData)
print("User count:",len(finalData))
for value in finalData:
	print("Name:",value["name"])
	print("Id:", value["id"])
	print("Attribute:",value["x"])
