import urllib
import re
import bs4
import ssl

#ignore SSL certificates
c=ssl.create_default_context()
c.check_hostname=False
c.verify_mode=ssl.CERT_NONE

l=raw_input('Enter URL: ')
f=urllib.urlopen(l,context=c)
mf=f.read()
soup=bs4.BeautifulSoup(mf,'html.parser')
u=[]
#get all img tags
tags=soup('img')
for t in tags:
#	print(t.get('href',None))
	u.append(str(t.get('src',None)))
lent=len(u)
print(lent)
i=0
while i<lent:

	if str(u[i])[0]=='h':
		urllib.urlretrieve(u[i],'image/'+str(i)+'.png')
	else:
		urllib.urlretrieve(str(l)+str(u[i]),'image/'+str(i)+'.png')
	i+=1
