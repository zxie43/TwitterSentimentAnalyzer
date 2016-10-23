import json, httplib, urllib, string, base64, ast

key = 'insert-your-key-here'
secret = 'insert-your-secret-key-here'

def getBearer(key, secret):
	#Ideally should url encode the key and secret,
	#but it will work ok without for now

	credentials = base64.b64encode(key + ':' + secret)
	headers = {'Authorization': 'Basic ' + credentials, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
	conn = httplib.HTTPSConnection('api.twitter.com')
	conn.request('POST', '/oauth2/token', 'grant_type=client_credentials', headers)
	response = conn.getresponse()
	bearer = ast.literal_eval(response.read())['access_token']
	return bearer

def getResults(bearer, hashtag):
	url = '/1.1/search/tweets.json?q=%23' + hashtag +'&count=100'
	headers = {'Authorization': 'Bearer ' + bearer}
	conn = httplib.HTTPSConnection('api.twitter.com')
	conn.request('GET', url, '', headers)
	response = conn.getresponse().read()
	return response

#print getResults(getBearer(key, secret), 'microsoft')