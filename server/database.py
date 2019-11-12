#####
# @file   : database.py
# @desc   : stores all data necessary
# @author : TBD
#####

# IMPORTS
import requests

# @class : database
# @desc  : loads in all data necessary for the database
class database:
    
    # CONSTANTS
	RAPID_URL = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market'
	STOCK_URL = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock'
	CHARTS_URL = RAPID_URL + '/get-charts'
	CHART_URL = STOCK_URL + '/v2/get-chart'
	QUOTES_URL = RAPID_URL + '/get-quotes'
	MOVERS_URL = RAPID_URL + '/get-movers'
	RAPID_HOST = 'apidojo-yahoo-finance-v1.p.rapidapi.com'
	RAPID_KEY = 'd491067285msh53abac8f5d4bed2p184db4jsn1546ca77d7fd'
	RAPID_HEADERS = {
		'x-rapidapi-host': RAPID_HOST,
		'x-rapidapi-key': RAPID_KEY
	}
 
	# @name : __init__
	# @desc : constructor for database
	def __init__(self):
		self.movers = {}
		self.charts = {}
		self.quotes = {}
		self.users = {}

	# @name : movers_params
	# @desc : return the params for the get-movers request
	def movers_params(self):
		return { 'region': 'US', 'lang': 'en' }

	# @name : charts_params
	# @desc : return the params for the get-charts request
	# @param : symbol = string (ex: 'MSFT')
	def charts_params(self, symbol, interval, rg):
		return {
			"region": "US",
			"lang": "en",
			"symbol": symbol,
			"interval": interval,
			"range": rg
		}
  
	# @name  : quotes_params
	# @desc  : return the params for the get-guotes request
	# @param : symbols = formatted string (ex: 'BAC,GOOGL,TSLA,MSFT')
	def quotes_params(self, symbols):
		return { 'region': 'US', 'lang': 'en', 'symbols': symbols }

	# @name : load_todays_movers
	# @desc : uses the YahooFinance API to load today's top movers
	def load_movers(self):
		self.movers = {}
		try:
			response = requests.request('GET', self.MOVERS_URL, headers=self.RAPID_HEADERS, params=self.movers_params())
		except Exception as ex:
			response = {}
		self.movers = response
  
	# @name : load_chart
	# @desc : uses the YahooFinance API to load charts
	def load_chart(self, symbol, interval, rg):
		try:
			response = requests.request('GET', self.CHARTS_URL, headers=self.RAPID_HEADERS, params=self.charts_params(symbol, interval, rg))
		except Exception as ex:
			return None
		self.charts[symbol] = response.json()

	# @name  : load_quotes
	# @desc  : uses the YahooFinance API to load quotes
	# @param : symbols = formatted string (ex: 'BAC,GOOGL,TSLA,MSFT')
	def load_quotes(self, symbols):
		self.quotes = {}
		try:
			response = requests.request('GET', self.QUOTES_URL, headers=self.RAPID_HEADERS, params=self.quotes_params(symbols))
		except Exception as ex:
			response = {}
		self.quotes = response
  
	# @name  : load_users
	# @desc  : loads the users from the data/users.dat file
	def load_users(self, file):
		self.users = {}
		f = open(file)
		for line in f:
			# Split the components
			line = line.rstrip()
			components = line.split('::')
			id = int(components[0])
			name = components[1]
			email = components[2]
			password = components[3]
			# Extract the stock information
			stockInfo = components[4]
			stocks = {}
			stockInfo = stockInfo.split('|')
			for elt in stockInfo:
				eltComponents = elt.split(':')
				stocks[eltComponents[0]] = int(eltComponents[1])
			# Insert into users dictionary
			self.users[id] = {
				'name': name,
				'email': email,
				'password': password,
				'stocks': stocks
			}
		f.close()

     
	# @name  : get_quote
	# @desc  : uses the YahooFinance API to load quotes
	def get_quote(self, symbol):
		if (symbol in self.quotes):
			return self.quotes[symbol]
		else:
			try:
				response = requests.request('GET', self.QUOTES_URL, headers=self.RAPID_HEADERS, params=self.quotes_params(symbol))
				self.quotes[symbol] = response
				return self.quotes[symbol]
			except Exception as ex:
				return None
		return None
  
	# @name  : get_quotes
	# @desc  : uses the YahooFinance API to load quotes
	def get_quotes(self):
		return self.quotes

	# @name  : get_users
	# @desc  : return the users
	def get_users(self):
		return self.users

	# @name  : get_user
	# @desc  : return the user
	def get_user(self, id):
		id = int(id)
		if id in self.users.keys():
			return self.users[id]
		else:
			return None

	# @name  : get_users
	# @desc  : return the user
	def get_users(self):
		return self.users
	
	# @name : delete_user
	# @desc : delete a specific user 
	def delete_user(self,id):
		self.users.pop(id,None)

	# @name : delete_user
	# @desc : delete a specific user 
	def delete_stock(self,stock):
		return self.users['stocks'].pop(stock,None)
			

# @name : main
# @desc : main driver for file
if __name__ == "__main__":
	db = database()
	db.load_movers()
