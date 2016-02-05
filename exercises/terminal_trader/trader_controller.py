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
		if self.user.check_account(login):
			self.user.load_accounts()
			if self.user.is_admin: 
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
		 	self.view.quit()
		else:
			self.invalid()
			self.menu()

	def search_stocks(self):
		self.choice = self.view.input_search()
		results = self.markit.company_search(self.choice)
		if len(results) <1:
			self.view.no_results
			self.menu()
		self.choose_company(results)

	def choose_company(self,results):
		company_index = self.view.choose_company(results)
		if not self.choose_company_check(company_index):
			self.view.invalid()
			self.choose_company(results)
		
		symbol = results[int(company_index["index"])-1]["Symbol"]
		self.user.symbol = symbol
		self.stock_details(symbol)

	def stock_details(self,symbol):
		result = self.markit.get_quote(symbol)
		self.view.print_details(result)
		self.stock_menu()

	def choose_company_check(self, company):
		# company = {"count":count,"index":index}
		for item in company["index"]:
			if not item.isdigit():
				return False 

		if int(company["index"]) >= 1 and int(company["index"]) <= company["count"]:
			return True 
		else:
			return False 

	def stock_menu(self):
		self.choice = self.view.stock_menu()
		if self.choice == "1":
			self.buy_stock()
		elif self.choice == "2":
			self.menu()
		else:
			self.view.invalid()
			self.menu()

	def buy_stock(self):
		self.choice = self.view.buy_stock_amount()

		count = 0 		
		if not self.choice.isdigit():
			self.view.invalid()
			self.buy_stock()
			count+= 1
		if not int(self.choice):
			self.view.invalid()
			self.buy_stock()
			count+=1
		if int(self.choice) <= 0:
			self.view.invalid()
			self.buy_stock()
			count+=1


		
		quote = self.markit.get_quote(self.user.symbol)
		price = quote["LastPrice"]
		
		
		if float(self.choice)*price+self.fee > self.user.funds:
			if count == 2:
				self.view.insufficient_funds()
				self.menu()
			else:
				count += 1 
				self.view.insufficient_funds()
				self.buy_stock()
		elif float(self.choice)*price + self.fee <= self.user.funds:
			self.user.funds -= float(self.choice)*price + self.fee
		self.user.buy_stock(self.choice)
		self.view.buy_confirmation(amount=self.choice,symbol = self.user.symbol,price = price,funds = self.user.funds)
		self.menu()

	def view_portfolio(self):
		self.user.load_accounts()
	
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