import requests
import json
import urllib2
content = urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/?limit=7').read()
coins = json.loads(content)
counter=1;
top7 = "---------------------\n"

for c in coins:
	price = json.dumps(c["price_usd"]).strip('"')
	top7 += str(counter) + "." + (json.dumps(c["symbol"]).strip('"')) + "     "  + '${:,.2f}'.format(eval(price)) + "\n"
	counter= counter + 1

top7 += "---------------------"
data = {"content": top7}
requests.post('https://discordapp.com/api/webhooks/404825031374405634/exHfIEsoOv6f6H13BSt0nNYgVJaCWkvmmcy6g4zAbd48WFrbazpdglRz2-xb1JV_E5KL', data=data)