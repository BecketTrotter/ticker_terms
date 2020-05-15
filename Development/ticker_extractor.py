
def pull_file(file):
	f = open(file)
	counter = 0
	tickers = []
	company_Names = []
	for x in f:
		counter += 1
		split_Words = x.split()
		if split_Words[0] != 'Symbol':
			tickers.append(split_Words[0])
			company_Names.append(' '.join(split_Words[1:]))
	return tickers, company_Names


def pull_file_after(file, ticker):
	f = open(file)
	counter = 0
	tickers = []
	company_Names = []
	reached = False

	for x in f:
		counter += 1
		split_Words = x.split()
		if split_Words[0] == ticker or reached:
			reached = True
			tickers.append(split_Words[0])
			company_Names.append(' '.join(split_Words[1:]))
	return tickers, company_Names