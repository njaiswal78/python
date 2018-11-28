# -*- coding: utf-8 -*-
import oauth2 as oauth
import httplib2
import time, os, simplejson
import urlparse
import BaseHTTPServer 
import datetime
from xml.etree import ElementTree as ET

 
consumer_key    =   '779llc1jtnh1rv'
consumer_secret =   'ORxeaAQKo1PTs4yU'
request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
access_token_url =  'https://api.linkedin.com/uas/oauth/accessToken'
authorize_url =     'https://api.linkedin.com/uas/oauth/authorize'

config_file   = '.service.dat'


http_status_print = BaseHTTPServer.BaseHTTPRequestHandler.responses
 

def get_auth():
	consumer = oauth.Consumer(consumer_key, consumer_secret)
	client = oauth.Client(consumer)

	try:
		filehandle = open(config_file)
		
	except IOError as e:
		filehandle = open(config_file,"w")
		print("We don't have a service.dat file, so we need to get access tokens!");
		content = make_request(client,request_token_url,{},"Failed to fetch request token","POST")
	
		request_token = dict(urlparse.parse_qsl(content))
		print "Go to the following link in your browser:"
		print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
	 
		oauth_verifier = raw_input('What is the PIN? ')
	 
		token = oauth.Token(request_token['oauth_token'],
		request_token['oauth_token_secret'])
		token.set_verifier(oauth_verifier)
		client = oauth.Client(consumer, token)
	 
		content = make_request(client,access_token_url,{},"Failed to fetch access token","POST")
		
		access_token = dict(urlparse.parse_qsl(content))
	 
		token = oauth.Token(
			key=access_token['oauth_token'],
			secret=access_token['oauth_token_secret'])
	 
		client = oauth.Client(consumer, token)
		simplejson.dump(access_token,filehandle)
	
	else:
		config = simplejson.load(filehandle)
		if ("oauth_token" in config and "oauth_token_secret" in config):
			token = 	oauth.Token(config['oauth_token'],
	    				config['oauth_token_secret'])
			client = oauth.Client(consumer, token)
		else:
			print("We had a .service.dat file, but it didn't contain a token/secret?")
			exit()
	return client

# Simple oauth request wrapper to handle responses and exceptions
def make_request(client,url,request_headers={},error_string="Failed Request",method="GET",body=None):
	if body:
		resp,content = client.request(url, method, headers=request_headers, body=body)
	else:
		resp,content = client.request(url, method, headers=request_headers)
	print resp.status
		
	if resp.status >= 200 and resp.status < 300:
		return content
	elif resp.status >= 500 and resp.status < 600:
		error_string = "Status:\n\tRuh Roh! An application error occured! HTTP 5XX response received."
		log_diagnostic_info(client,url,request_headers,method,body,resp,content,error_string)
		
	else:
		status_codes = {403: "\n** Status:\n\tA 403 response was received. Usually this means you have reached a throttle limit.",
						401: "\n** Status:\n\tA 401 response was received. Usually this means the OAuth signature was bad.",
						405: "\n** Status:\n\tA 405 response was received. Usually this means you used the wrong HTTP method (GET when you should POST, etc).",
						400: "\n** Status:\n\tA 400 response was received. Usually this means your request was formatted incorrectly or you added an unexpected parameter.",
						404: "\n** Status:\n\tA 404 response was received. The resource was not found."}
		if resp.status in status_codes:
			log_diagnostic_info(client,url,request_headers,method,body,resp,content,status_codes[resp.status])
		else:
			log_diagnostic_info(client,url,request_headers,method,body,resp,content,http_status_print[resp.status][1])
	

	
def get_json():
	data=['If you look at what you have in life, you’ll always have more. If you look at what you don’t have in life, you’ll never have enough. —Oprah Winfrey','Remember no one can make you feel inferior without your consent. —Eleanor Roosevelt','I can’t change the direction of the wind, but I can adjust my sails to always reach my destination. —Jimmy Dean','“To handle yourself, use your head; to handle others, use your heart.” —Eleanor Roosevelt','Too many of us are not living our dreams because we are living our fears. —Les Brown','Twenty years from now you will be more disappointed by the things that you didn’t do than by the ones you did do, so throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails. Explore, Dream, Discover. —Mark Twain','I’ve missed more than 9000 shots in my career. I’ve lost almost 300 games. 26 times I’ve been trusted to take the game winning shot and missed. I’ve failed over and over and over again in my life. And that is why I succeed. —Michael Jordan','Strive not to be a success, but rather to be of value. —Albert Einstein','I am not a product of my circumstances. I am a product of my decisions. —Stephen Covey','When everything seems to be going against you, remember that the airplane takes off against the wind, not with it. —Henry Ford','The most common way people give up their power is by thinking they don’t have any. —Alice Walker','The most difficult thing is the decision to act, the rest is merely tenacity. —Amelia Earhart','It is during our darkest moments that we must focus to see the light. —Aristotle Onassis','Don’t judge each day by the harvest you reap but by the seeds that you plant. —Robert Louis Stevenson','It is during our darkest moments that we must focus to see the light. —Aristotle Onassis'
	,'Don’t judge each day by the harvest you reap but by the seeds that you plant. —Robert Louis Stevenson'
	,'The only way to do great work is to love what you do. —Steve Jobs'
	,'Change your thoughts and you change your world. —Norman Vincent Peale'
	,'The question isn’t who is going to let me; it’s who is going to stop me. —Ayn Rand'
	,'If you hear a voice within you say "you cannot paint," then by all means paint and that voice will be silenced. —Vincent Van Gogh'
	,'Build your own dreams, or someone else will hire you to build theirs. —Farrah Gray'
	,'Remember that not getting what you want is sometimes a wonderful stroke of luck. —Dalai Lama'
	,'You can’t use up creativity. The more you use, the more you have. —Maya Angelou;'
	,'I have learned over the years that when one’s mind is made up, this diminishes fear. —Rosa Parks'
	,'I would rather die of passion than of boredom. —Vincent van Gogh'
	,'A truly rich man is one whose children run into his arms when his hands are empty. —Unknown'
	,'A person who never made a mistake never tried anything new.——Albert Einstein'
	,'What’s money? A man is a success if he gets up in the morning and goes to bed at night and in between does what he wants to do. —Bob Dylan'
	,'I have been impressed with the urgency of doing. Knowing is not enough; we must apply. Being willing is not enough; we must do. —Leonardo da Vinci'
	,'If you want to lift yourself up, lift up someone else. —Booker T. Washington'
	,'Limitations live only in our minds. But if we use our imaginations, our possibilities become limitless. —Jamie Paolinetti'
	,'If you’re offered a seat on a rocket ship, don’t ask what seat! Just get on. —Sheryl Sandberg'
	,'Certain things catch your eye, but pursue only those that capture the heart. —Ancient Indian Proverb'
	,'When one door of happiness closes, another opens, but often we look so long at the closed door that we do not see the one that has been opened for us. —Helen Keller'
	,'Everything has beauty, but not everyone can see. —Confucius'
	,'How wonderful it is that nobody need wait a single moment before starting to improve the world. —Anne Frank'
	,'When I was 5 years old, my mother always told me that happiness was the key to life. When I went to school, they asked me what I wanted to be when I grew up. I wrote down “happy”. They told me I didn’t understand the assignment, and I told them they didn’t understand life. —John Lennon'
	,'The only person you are destined to become is the person you decide to be. —Ralph Waldo Emerson'
	,'We can’t help everyone, but everyone can help someone. —Ronald Reagan'
	,'Everything you’ve ever wanted is on the other side of fear. —George Addair'
	,'We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light. —Plato'
	,'Nothing will work unless you do. —Maya Angelou'
	,'“I alone cannot change the world, but I can cast a stone across the water to create many ripples.” —Mother Teresa'
	,'What we achieve inwardly will change outer reality. —Plutarch','“If you are on social media, and you are not learning, not laughing, not being inspired or not networking, then you are using it wrong.”','“A huge number of jobs that are filled are never advertised to the public, or if they are, they’re filled by people who have a connection to the employer.” ','“Active participation on LinkedIn is the best way to say, Look at me!, without saying,- Look at me!']
	#print type(data)
	#random_numer=n.random.randint(0,len(data))
	today = datetime.date.today()
	someday = datetime.date(2018, 11, 20)
	diff = today-someday
	random_numer=diff.days
	
	comment_text=data[random_numer]
	visibility = "anyone";
	
	share_object = {
					"comment":comment_text,
				
					"visibility": {
						"code":visibility
					}
	}
	
	json_content = simplejson.dumps(share_object)
	return json_content


#if __name__ == "__main__":
	# Get authorization set up and create the OAuth client
#	client = get_auth()
	
	
	# Simple profile call, returned in JSON
#	print "\n********Get the profile in JSON********"
#	response = make_request(client,"http://api.linkedin.com/v1/people/~",{"x-li-format":'json'})
#	print response
	
#	json_content = get_json()
	
	
	#print "\n********Write to the share - using JSON********"
	#api_url = "http://api.linkedin.com/v1/people/~/shares";
	#response = make_request(client,api_url,{'Content-Type':'application/json'},"Failed to post share","POST",json_content)#
#	exit();
	
	