import urllib.request, urllib.parse, urllib.error
import ssl, re
from bs4 import BeautifulSoup
from bs4.element import Comment
import nltk
from nltk.corpus import stopwords
import math
#ssl certificates for https *\"comments\">
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode

sWords = set(stopwords.words('english'))

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

anchor=[]
count = int(input("Enter the number of pages to visit for cluster- ")) 
url = input("Enter -")
# count=int(input("Enter count: "))
# position =int(input("Enter position: "))
# for i in range(count):
dataWords = []

for i in range(count) :
	dataWords.append({})
	html = urllib.request.urlopen(url,context=ctx).read()

	textPage = text_from_html(html)
	words = textPage.split()
	for word in words:
		dataWords[i][word] = dataWords[i].get(word, 0)+ 1

	soup = BeautifulSoup(html, 'html.parser')
	tags = soup("a")
	for tag in tags:
		x = str(tag.get("href"))
		if x.startswith('http'):
			anchor.append(x)

	url = anchor[10]
	anchor = []

mainData = {} 
sumList = []

for i in range(count) :
	total = 0
	for word in dataWords[i]:
		total += dataWords[i][word]
		mainData[word] = mainData.get(word, 0) + 1

	sumList.append(total)

for i in range(count):
	for word in dataWords[i]:
		print(word+" "+str(dataWords[i][word]/sumList[i]))

print("\n\n\n\n\n")
for word in mainData:
	print(word + "-->"+ str(math.log(count/mainData[word])))



