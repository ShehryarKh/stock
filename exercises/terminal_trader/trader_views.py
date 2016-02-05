class View:

	def welcome(self):
		print("Welcome to Trader Duels")

	def login(self):
		username = input("Enter username:")
		password = input("Enter password:")
		login = {"username":username, "password":password}
		return login 

	def no_account(self):
		print("Username or password incorrect")

	def menu(self,funds):
		print("\nMain Menu")
		# show user funds and portfolio value 
		print("\nAvailable funds: ${}".format(funds))
		choice = input("""
[1] search stocks
[2] view portfolio
[3] quit 
""")
		return choice 

	def invalid(self):
		print("-----INVALID INPUT-----")

	def input_search(self):
		input_search = input("Enter stock to search:")
		return input_search

	def choose_company(self,result):
		count = 1 
		for company in result:
			print("[{}]\tsymbol:{}\tname:{}".format(count,company["Symbol"], company["Name"]))
			count += 1 
		count -= 1 
		index = input("Enter choice index number:")
		dic = {"count":count,"index":index}
		return dic 

	def print_details(self,result):
		for key,values in result.items():
			print("{}:{}".format(key,values))

	def stock_menu(self):
		choice = input("""
			[1] Buy Stock
			[2] Main Menu
""")
		return choice 

	def buy_stock_amount(self):
		num = input("BUY:Enter number of shares:")
		return num 

	def insufficient_funds(self):
		print("-----INSUFFICIENT FUNDS-----")

	def buy_confirmation(self,amount,price, symbol,funds):
		print(
"""
Confirmation:

	Bought {} shares of {} @ ${} each.

	Subtotal ${}
	+ $10 Buy fee
	_____________
	Total ${}

Your Remaning Funds are ${}				
""".format(amount,symbol,price,float(amount)*price,float(amount)*price+10,funds))

	def print_portfolio(self,list_,portfolio_val,funds):
		print("_____________________________")
		print("\nMy Portfolio")
		print("\nCurrent Value ${}\n".format(portfolio_val))
		print("Worth of all assets:${}\n".format(funds+portfolio_val))
		for item in list_:
			print("{symbol}|{num_shares}|${total}".format(**item))
		print("_____________________________")



	def quit(self):
		print("Goodbye!")

	def no_results(self):
		print("----None Found----")
