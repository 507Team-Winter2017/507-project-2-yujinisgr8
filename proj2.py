#proj2.py


#### Problem 1 ####
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
 
r = urllib.request.urlopen('http://www.nytimes.com', context=ctx).read()
soup1 = BeautifulSoup(r,'html.parser')


def headings(): 
	n=0
	for story_heading in soup1.find_all(class_="story-heading"): 
		n += 1
		if n > 10:
			break
		if story_heading.a: 
			print(story_heading.a.text.replace("\n", " ").strip())
		else:
			print(story_heading.contents[0].strip())

print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')
headings()


#### Problem 2 ####
url2 = urllib.request.urlopen('https://www.michigandaily.com', context=ctx).read()
soup2 = BeautifulSoup(url2, 'html.parser')

def most_read():
	for most in soup2.find_all(class_="panel-pane pane-mostread"):
		for li in most(class_="item-list"):
			print (li.get_text())

print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')
most_read()


#### Problem 3 ####
url3 = urllib.request.urlopen('http://newmantaylor.com/gallery.html', context=ctx).read()
soup3 = BeautifulSoup(url3, 'html.parser')
def img_alt():
	for image in soup3.find_all("img"):
		if image.get('alt')==None:
			print('No alternative text provided!')
		else:
			print(image.get('alt'))

print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")
img_alt()


#### Problem 4 ####

def email():
	base_url='https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
	base_url_prof='https://www.si.umich.edu'
	n=0
	for i in range(6):
		if i == 0:
			req=urllib.request.Request(base_url, None, {'User-Agent': 'SI_CLASS'})
		else:
			req=urllib.request.Request(base_url + '&page='+ str(i), None, {'User-Agent': 'SI_CLASS'})
		url4=urllib.request.urlopen(req, context=ctx).read()
		soup4=BeautifulSoup(url4,'html.parser')
		for link in soup4.find_all("a", string= "Contact Details"):
			# print(link.get('href'))
			req2=urllib.request.Request(base_url_prof + link.get('href'), None, {'User-Agent': 'SI_CLASS'})
			url_prof=urllib.request.urlopen(req2, context=ctx).read()
			soup5=BeautifulSoup(url_prof,'html.parser')
			for email in soup5.find_all(class_='field field-name-field-person-email field-type-email field-label-inline clearfix'):
				mail=str.split(email.get_text())
				n+=1
				print (str(n) + " " + mail[1])

print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")
email()

