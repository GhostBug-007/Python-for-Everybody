import re
openFile=open("extractFile.txt","r")
total=0
for line in openFile:
	x=re.findall("[0-9]+",line)
	x=list(map(int,x))
	# length=len(x)
	total+=sum(x)
print(total)
