import requests

class Markit:
	def __init__(self):
		self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json"
		self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json"

	def company_search(self,search_term):
		payload = {"input": search_term}
		companies = requests.get(self.lookup_url, params = payload).json()
		return companies 

	def get_quote(self,symbol):
		payload = {"symbol": symbol}
		quote = requests.get(self.quote_url, params = payload).json()
		return quote 