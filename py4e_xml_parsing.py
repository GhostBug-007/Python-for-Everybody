import xml.etree.ElementTree as ET
input = ''' 
<person>
	<name>Prateek</name>
	<phone type="personal">+91-7891676156</phone>
	<email hide="yes" />
</person>'''
tree = ET.fromstring(input)
print("Name: ",tree.find("name").text)
print("Contact: ",tree.find("phone").text)
print("Contact type: ",tree.find("phone").get("type"))
print("Attribute: ",tree.find("email").get("hide"))