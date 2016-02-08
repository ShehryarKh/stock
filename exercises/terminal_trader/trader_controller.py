from trader_views import View 
from trader_models import *
from wrapper import Markit

class Controller:
	def __init__(self):
		self.view = View()
		self.user = UserDatabase()
		self.markit = Markit()
		self.quit = ["quit","q", "Quit","QUIT"]
		self.choice = ''
		self.fee = 10 

	def run(self):
		self.view.welcome()
		self.login()

	def login(self): 
		login = self.view.login()
		if self.user.check_and_load_account(login):
			if self.user.is_admin:
				self.view.welcome_admin(self.user.username)
				self.admin_menu()
			else:
				self.menu()
		else:
			self.view.no_account()
			self.login()

	def admin_menu(self):
		pass

	def menu(self):
		self.choice = self.view.menu(self.user.funds)
		if self.choice == "1":
		 	self.search_stocks()
		elif self.choice == "2":
		 	self.view_portfolio()
		elif self.choice == "3":
		 	self.sell_stock()
		elif self.choice == "4":
			self.search_stocks()
		elif self.choice == "5":
			self.view.quit()
		else:
			self.view.invalid()
			self.menu()

	def search_stocks(self):
		self.choice = self.view.input_search()
		results = self.markit.company_search(self.choice)
		if len(results) <1:
			self.view.no_results
			self.menu()
		self.choose_company(results)

	

	def sell_stock(self):
		# self.choice  ={"symbol":symbol,"num_shares":num_shares}
		self.choice = self.view.sell_stock()
		if not self.sell_stock_check(self.choice):
			self.menu()
		self.choice["symbol"].upper()
		result = self.markit.get_quote(self.choice["symbol"])
		total_sale_price = result["LastPrice"]*float(self.choice["num_shares"])
		self.user.funds += round(total_sale_price,2)
		self.user.funds -= self.fee
		self.user.update_stocks(self.choice) 
		self.user.load_accounts()
		self.view.sale_confirmation(self.choice,funds=self.user.funds,price = result["LastPrice"],sub = total_sale_price)
		self.menu()
		

	def sell_stock_check(self,sale):
		if not sale["num_shares"].isdigit():
			self.view.no_digits_error()
			return False
		if not sale["symbol"].isalpha():
			self.view.not_alpha_error()
			return False 
		sale["symbol"] = sale["symbol"].upper()

		for symbol,num_shares in self.user.stocks:
			if sale["symbol"] == symbol and int(sale["num_shares"]) <= num_shares:
				return True
		self.view.invalid_amount()
		return False

	def choose_company(self,results):
		company_index = self.view.choose_company(results)
		if not self.choose_company_check(company_index):
			self.view.invalid()
			self.choose_company(results)
		
		symbol = results[int(company_index["index"])-1]["Symbol"]
		self.stock_details(symbol)

	def stock_details(self,symbol):
		result = self.markit.get_quote(symbol)
		self.view.print_details(result)
		self.stock_menu(symbol)

	def choose_company_check(self, company):
		# company = {"count":count,"index":index}
		for item in company["index"]:
			if not item.isdigit():
				return False 

		if int(company["index"]) >= 1 and int(company["index"]) <= company["count"]:
			return True 
		else:
			return False 

	def stock_menu(self,symbol):
		self.choice = self.view.stock_menu()
		if self.choice == "1":
			self.buy_stock(symbol)
		elif self.choice == "2":
			self.menu()
		else:
			self.view.invalid()
			self.menu()

	def buy_stock(self,symbol):
		self.choice = self.view.buy_stock_amount()
		if not self.buy_stock_check(self.choice):
			self.view.invalid()
		quote = self.markit.get_quote(symbol)
		price = quote["LastPrice"]
		
		
		if round(float(self.choice),2)*price+self.fee > self.user.funds:
			self.view.insufficient_funds()
			self.buy_stock()
		elif round(float(self.choice),2)*price + self.fee <= self.user.funds:
			self.user.funds -= round(float(self.choice),2)*price + self.fee
		self.user.buy_stock(self.choice,symbol)
		self.user.load_accounts()
		self.view.buy_confirmation(amount=self.choice,symbol = self.user.symbol,price = price,funds = self.user.funds)
		self.menu()

	def buy_stock_check(self,amount):			
		if not amount.isdigit():
			self.view.invalid()
			self.buy_stock()
			return False 
			
		elif not int(amount):
			self.view.invalid()
			self.buy_stock()
			return False 
			
		elif int(amount) <= 0:
			self.view.invalid()
			self.buy_stock()
			return False
		else:
			return True 
			


		
		

	def view_portfolio(self):
		list_=[]
		portfolio_val = 0 
		for symbol,num_shares in self.user.stocks:
			company = self.markit.get_quote(symbol)
			price = company["LastPrice"]
			total = price*float(num_shares)
			portfolio_val += total
			a_dic = {"symbol":symbol,"num_shares":num_shares,"total":total}
			list_.append(a_dic)

		self.view.print_portfolio(list_,portfolio_val,self.user.funds)
		self.menu()
			




	


c = Controller()
c.run()