from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


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

url = input("Enter the url--> ") 
html = urllib.request.urlopen(url).read()
tex = text_from_html(html)

dictionary = {} 

words = tex.split()

for word in words :
	dictionary[word] = dictionary.get(word, 0) + 1

print(dictionary)