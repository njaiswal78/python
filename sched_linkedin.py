import linkedin_p
import time
import win32api

i=0
print 'LinkedIn Post Quote Intitated ...'
while 1:

	a=time.localtime()
	b=a[3]
	if b==16:
		result = win32api.MessageBox(None,"It is time to post linkedin status, please make sure you are connected to Internet", "LinkedIn PostQuote",1)
		
		if result==1:
			try:
			
				
				client = linkedin_p.get_auth()
				#print "\n********Get the profile in JSON********"
				#response = linkedin_p.make_request(client,"http://api.linkedin.com/v1/people/~",{"x-li-format":'json'})
				#print response
				
				json_content = linkedin_p.get_json()
		
		
				#print "\n********Write to the share - using JSON********"
				api_url = "http://api.linkedin.com/v1/people/~/shares";
				response = linkedin_p.make_request(client,api_url,{'Content-Type':'application/json'},"Failed to post share","POST",json_content)
				win32api.MessageBox(None,"Posted Successfully", "LinkedIn PostQuote",0x00001000)
			except:
				win32api.MessageBox(None,"You are on Intranet, hence cannot post status update on linkedin", "LinkedIn PostQuote",0x00001000)
			
			
		else:
			print "Posting today is cancelled"
	else:
		print "This is not posting hour"
	time.sleep(1500)
	#client = linkedin_p.get_auth()
		#print "\n********Get the profile in JSON********"
		#response = linkedin_p.make_request(client,"http://api.linkedin.com/v1/people/~",{"x-li-format":'json'})
		#print response  
		