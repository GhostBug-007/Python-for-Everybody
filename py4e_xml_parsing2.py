import xml.etree.ElementTree as ET
input = ''' <stuff>
	<users>
		<user x='1'>
			<id>001</id>
			<name>Prateek</name>
		</user>
		<user x='5'>
			<id>007</id>
			<name>Lorry</name>
		</user>
		<user x='6'>
			<id>008</id>
			<name>Prateek</name>
		</user>
		<user x='9'>
			<id>009</id>
			<name>Lorry</name>
		</user>
	</users>
</stuff>'''

input=ET.fromstring(input)
lst = input.findall("users/user")
print("Count User:",len(lst))
for item in lst:
	print("Id No. -",item.find("id").text,end=" ")
	print(item.find("name").text)
	print("Attribute -",item.get('x'))


