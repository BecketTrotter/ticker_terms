from people_scraper import get_key_people
from name_scraper import name_from_yahoo_finance
from database_management import create_table, add_ticker, commit_close, open_connection
from ticker_extractor import pull_file, pull_file_after


def generate_add(ticker, c_name, conn, c):
	#enter one company into the db
	null_List = ['NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL']
	key_people = get_key_people(ticker)
	

	if key_people == -1:
		raise Exception('error pulling key people for {}'.format(c_name))
	
	if key_people == 0:
		print("key_people not found")
		
	key_people = key_people[:6]
	padding = null_List[:(6 - len(key_people))]
	entry = tuple([ticker] + [c_name] + key_people + padding)

	add_ticker(entry, c)
	conn.commit()

def add_file(file):
	#add a whole while to the db
	tickers, c_names = pull_file(file)
	if len(tickers) != len(c_names):
			print("error in len")

	conn, c = open_connection("DB/Stocks.db")

	for x in range(len(tickers)):
		try:
			generate_add(tickers[x], c_names[x], conn, c)
			print("Success on {}".format(c_names[x]))

		except:
			print("Error on Name: {} ${}".format(c_names[x], tickers[x]))

		if x % 50 == 0:
			conn.commit()
			print("\n\ncommitted")

def pull_after_ticker(file, ticker):
	#add all tickers after a ticker in a file
	#useful if your upload is stopped
	tickers, c_names = tickers_After(file, ticker.upper())
	conn, c = open_connection("DB/Stocks.db")

	for x in range(len(tickers)):
		generate_add(tickers[x], c_names[x], conn, c)

		print("Success on {}".format(c_names[x]))

	conn.commit()