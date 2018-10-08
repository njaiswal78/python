import urllib
import re
import bs4
import ssl

#ignore SSL certificates
c=ssl.create_default_context()
c.check_hostname=False
c.verify_mode=ssl.CERT_NONE

l=raw_input('Enter URL: ')
ct=raw_input('Enter Count: ')
pos=raw_input('Enter Position: ')
f=urllib.urlopen(l,context=c)
mf=f.read()
#a=re.findall('[a-zA-Z]+',mf)
#print a.count('href')

#webpage extraction using beautifulsoup parser

soup=bs4.BeautifulSoup(mf,'html.parser')

#get all anchor tags
tags=soup('a')
#print type(tags)
#i=0
u=[]
ct=int(ct)
while ct>0:

	for t in tags:
#	print(t.get('href',None))
		u.append(str(t.get('href',None)))

	print('Retreiving: '+u[int(pos)-1])
	f=urllib.urlopen(u[int(pos)-1],context=c)
	mf=f.read()
	soup=bs4.BeautifulSoup(mf,'html.parser')
	tags=soup('a')
	ct-=1
	u=[]



#print(len(u))
#print(u)
#print('URL')
#print(str(u))

#Assignment
#count=0
#tagsAssignment=soup('span')
#for t in tagsAssignment:
#	count+=int(t.contents[0])

#print(count)


