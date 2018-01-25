import requests
import collections
import json
import urllib2
webhook_url = 'https://discordapp.com/api/webhooks/406086423335141376/DDZ8soXvYXYgG9oWcJnFjsl9NlZc6UME3E_UAln9Y0jD4IcmN7AA7ISP4j8lN2DjhYHv'
content = urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/?limit=0').read()
coins = json.loads(content)
orderedDictionary = {}
top7 = "---------------------\n"

for c in coins:
	symbol = json.dumps(c["symbol"]).strip('"')
	try:
		one_hr =json.dumps(c["percent_change_1h"]).strip('"')
		one_hr=float(one_hr)
		orderedDictionary[one_hr] = symbol

	except:
		print("data is null")

orderedDictionary = collections.OrderedDict(sorted(orderedDictionary.items()))
print orderedDictionary	

for x in range(1,8):
	top7 += str(x) + "." + orderedDictionary.values()[-x] + "            "  + str('{0:.2f}%'.format(orderedDictionary.keys()[-x]))+  "\n"
	

top7 += "---------------------"

print top7
data = {"content": top7}
requests.post(webhook_url, data=data)