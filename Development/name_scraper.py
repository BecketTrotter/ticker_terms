import requests

def name_from_yahoo_finance(symbol):
	#gen company_names names from yahoo finance
	base_url = 'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en'
	base_url = base_url.format(symbol)
	return(requests.get(base_url).json()['ResultSet']['Result'][0]['name'])