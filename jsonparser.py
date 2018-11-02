import urllib
import json
a=raw_input('Enter location: ')
print('Retreiving '+str(a))
b=urllib.urlopen(a).read()
print('Retreived '+str(len(b))+' characters')
c=json.loads(b)
d=c['comments']
print('Count: '+str(len(d)))
s=0
for i in d:
	s=s+int(i['count'])
print('Sum: '+str(s))	
