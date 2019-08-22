from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import math


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

url1 = input("Enter url1--> ") 
url2 = input("Enter url2--> ")
html1 = urllib.request.urlopen(url1).read()
tex1 = text_from_html(html1)

dictionary1 = {} 

words1 = tex1.split()

for word in words1 :
	dictionary1[word] = dictionary1.get(word, 0) + 1

html2 = urllib.request.urlopen(url2).read()
tex2 = text_from_html(html2)
print(dictionary1)

dictionary2 = {}

words2 = tex2.split() 

for word in words2 :
	dictionary2[word] = dictionary2.get(word, 0) + 1
print(dictionary2)
#a = {'s' : 2, 'g' : 1}
#b = {'s' : 4, 'r' : 5}
totalSum = 0
mod1, mod2 = 0,0
for i in dictionary1.keys():
	for j in dictionary2.keys():
		if i == j :
			totalSum += dictionary1[i] * dictionary2[j]

for i in dictionary1.keys() :
	mod1 += dictionary1[i]*dictionary1[i]
print(mod1)

for i in dictionary2.keys() :
	mod2 += dictionary2[i]*dictionary2[i]

mod1 = math.sqrt(mod1)
mod2 = math.sqrt(mod2)
cosO = totalSum/(mod1 * mod2)
print("The similarity between the documents is " + str(cosO*100) + "%")	
	
			
#print(len(dictionary1))
#print(len(dictionary2))


