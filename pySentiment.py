# Simple program that demonstrates how to invoke Azure ML Text Analytics API: key phrases, language and sentiment detection.
import urllib2
import urllib
import sys
import base64
import json
import TwitterTest

key = 'insert-your-key-here'
secret = 'insert-your-secret-key-here'

output = json.loads(TwitterTest.getResults(TwitterTest.getBearer(key, secret), 'microsoft'))


length1 = len(output["statuses"])

textonly = []
dateonly = []
jsontext = []
for i in range(0, length1):
	textonly.append(output["statuses"][i]["text"].encode("utf-8"))
	dateonly.append(output["statuses"][i]["created_at"].encode("utf-8"))
	jsontext.append({'id': str(i), 'text' :textonly[i], 'date' :dateonly[i]})

jsontext = json.dumps(jsontext)
print jsontext
jsontext = '{"documents":'+jsontext+'}\''
print jsontext

#print output
f = open("output.txt",'w')
print >>f, jsontext

base_url = 'https://westus.api.cognitive.microsoft.com/'

account_key = 'a6444726d47c4f2eada3df1cce394065'

headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}
            
num_detect_langs = 1;

# Detect sentiment.
batch_sentiment_url = base_url + 'text/analytics/v2.0/sentiment'
req = urllib2.Request(batch_sentiment_url, jsontext, headers) 
response = urllib2.urlopen(req)
result = response.read()
obj = json.loads(result)
for sentiment_analysis in obj['documents']:
    print('Sentiment ' + str(sentiment_analysis['id']) + ' score: ' + str(sentiment_analysis['score']))