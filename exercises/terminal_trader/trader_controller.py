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
# 	buying stocks
	def buy_stock(self):
		option = self.view.buy_main()
		if option == '1':
			num_stocks = self.view.display_check()
			price = self.market.recent_quote['LastPrice']*(num_stocks)
			print("thats a total of ${}".format(price))
			self.view.display_option()
			return price

	
	def purchase(self, price):



c = controller()
c.run()
