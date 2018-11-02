import json
import re
#import time
#import subprocess

#close_time=time.time()+*60
#
#while True:	
#	with open("output.txt", "w+") as output:
#		subprocess.call(["python", "C:/Users/Downloads/Python/python/twbrand.py"], stdout=output);
#	if time.time()>close_time:
#		break


f=open("C:\\Users\\Jaiswal7N\\Downloads\\Python\\python\\twdata.txt","r")
a=f.readlines()
b=[]
for i in range(len(a)):
	if (i%2)==0:
		b.append(a[i])
#print(len(b))
#print type(b)
d=[]
for j in range(len(b)):
	c=json.loads(b[j])
	d.append(c['text'].encode("utf-8"))
#print c['text'].encode("utf-8")
#print json.dumps(c,indent=4)
e=re.findall('[a-zA-Z]+',str(d).lower())
print ("Vodafone: "+str(e.count('vodafone')))
print ("Airtel: "+str(e.count('airtel')))
print ("Jio: "+str(e.count('jio')))
	
#	if time.time()>close_time:
#		break
