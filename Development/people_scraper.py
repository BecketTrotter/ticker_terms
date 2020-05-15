import requests
from bs4 import BeautifulSoup

def get_key_people(symbol):
	#pull list of execs from yahoo fin
	base_url = 'https://finance.yahoo.com/quote/{0}/profile?p={0}'
	url = base_url.format(symbol)
	page = requests.get(url)
	

	if page.url.find("lookup") != -1 or page.url != url:
		return -1
	soup = BeautifulSoup(page.text, 'html.parser')
	soup = soup.body

	tags = [tag.name for tag in soup.find_all('td', class_ = "Ta(start)")]

	table_text = soup.findAll('td', class_ = "Ta(start)")

	titles = ["Mr.", "Mrs.", "Ms."]
	key_people = []

	for x in table_text:
		split_words = x.text.split()
		if split_words[0] in titles:
			key_person = ' '.join(split_words[1:]) #takes out Mr. Mrs. Ms.
			key_people.append(key_person)

	return key_people