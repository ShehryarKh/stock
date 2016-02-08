import sqlite3
from trader_views import View
from trader_models import *
from wrapper import *

class controller():

	def __init__(self):
		self.view = View()
		self.user = UserDatabase()
		self.quit = ["quit", "q"]
		self.choice = ''
		self.market = Markit()

		#self.num_stocks = 

	def run (self):
		self.view.start()
		self.login_()
		self.stock_price()
		self.buy_stock()

		#self.menu()

	def login_(self):
		login = self.view.login()
		if self.user.check_account(login):
			self.user.load_accounts()
			if self.user.premission_level == 0:
				self.admin_menu()
			else:
				self.menu()

		else:
			self.view.invalid_accounts()
			self.login_()

	def admin_menu(self):
		self.view.admin_login()

	def menu(self):
		self.view.user_login()
		menu_choice = self.view.main_menu()
		if menu_choice == '1':

			company_name = self.view.search_term()
			results = self.search_stock(company_name)

			self.view.print_results(results)

			return results
			#print(results)s

			
	def stock_price(self):
		symbol = self.view.which_result()
		price_results = self.get_quote2(symbol)

		self.view.show_value(price_results)
		self.view.buy_main()
		#return price_results

	def search_stock(self,company_name):
		companies = self.market.company_search(company_name)
		return companies

	def get_quote2(self,symbol):
		quote = self.market.get_quote(symbol)
		return quote

	def search_t(self):
		self.view.search_term()

	def stock_amount(self):
		num_stocks = self.view.how_many()
		return num_stocks

	def price(self,x):
		price = self.market.recent_quote['LastPrice'] * x
		self.view.total_cost(price)
		return price

	#def price_p(self):
	#	price = self.market.recent_quote['LastPrice']*(self.stock_amount())
	#	return price

	def symbol(self):
		symbol = self.market.recent_quote['Symbol']
		return symbol

	def total_price(self):
		total_price = self.price(self.stock_amount())
		return total_price


# 	buying stocks
	def buy_stock(self):
		#buy or go main meny
		option = self.view.buy_main()
		if option == '1':
			#how many stock you waana purchase
			total_price = self.price(self.stock_amount())

			yes = self.view.display_option()
			if yes == 'y':
				self.purchase(total_price)
				self.view.you_bought(self.stock_amount(), self.symbol(), self.price(self.stock_amount))
				print(self.user.funds)
	
	def purchase(self, cost):
		while cost > self.user.funds:
			self.view.insufficient_funds()
			# code to get user to choose num stock again
		if cost < self.user.funds:
			self.user.funds -= cost
			self.user.update_users(self.user.funds)
			return self.user.funds







c = controller()
c.run()
