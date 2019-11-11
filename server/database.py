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
	CHARTS_URL = RAPID_URL + '/get-charts'
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
	def charts_params(self, symbol):
		return {
			"comparisons": "^GDAXI,^FCHI",
			"region": "US",
			"lang": "en",
			"symbol": symbol,
			"interval": "5m",
			"range": "1d"
		}
  
	# @name  : quotes_params
	# @desc  : return the params for the get-guotes request
	# @param : symbols = formatted string (ex: 'BAC,GOOGL,TSLA,MSFT')
	def quotes_params(self, symbols):
		return { 'region': 'US', 'lang': 'en', 'symbols': symbols }

	# @name : load_todays_movers
	# @desc : uses the YahooFinance API to load today's top movers
	def load__movers(self):
		self.movers = {}
		response = requests.request('GET', self.MOVERS_URL, headers=self.RAPID_HEADERS, params=self.movers_params())
		print(response.text) # @TODO : don't just print
  
	# @name : load_chart
	# @desc : uses the YahooFinance API to load charts
	def load_chart(self, symbol):
		response = requests.request('GET', self.CHARTS_URL, headers=self.RAPID_HEADERS, params=self.charts_params(symbol))
		print(response.text) # @TODO : don't just print

	# @name : load_charts
	# @desc : uses the YahooFinance API to load charts
	# @TODO : determine how to load several charts, also get rid of BAC
	def load_charts(self):
		response = requests.request('GET', self.CHARTS_URL, headers=self.RAPID_HEADERS, params=self.charts_params('BAC'))
		print(response.text) # @TODO : don't just print

# @name : main
# @desc : main driver for file
if __name__ == "__main__":
	db = database()
	db.load_movers()
