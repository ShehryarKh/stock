class View:

	def welcome(self):
		print("Welcome to Trader Duels")

	def welcome_admin(self,username):
		print("Welcome Admin {}".format(username))

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
		print("\nAvailable funds: ${}".format(round(funds,2)))
		choice = input("""
[1] Search stock
[2] View portfolio
[3] Sell stock
[4] Buy stock
[5] Quit 
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
Buy Confirmation:

	Bought {} shares of {} @ ${} each.

	Subtotal ${}
	+ $10 Buy fee
	_____________
	Total ${}

Your Remaning Funds are ${}				
""".format(amount,symbol,price,float(amount)*price,float(amount)*price+10,funds))

	def sale_confirmation(self,dic,price,sub,funds):
		print(
"""
Sale Confirmation:

	Sold {} shares of {} @ ${} each.

	Subtotal ${}
	- $10 Buy fee
	_____________
	Total ${}

Your Remaning Funds are ${}				
""".format(dic["num_shares"],dic["symbol"],price,sub,sub-10,round(funds,2)))


	def print_portfolio(self,list_,portfolio_val,funds):
		print("_____________________________")
		print("\nMy Portfolio")
		print("\nCurrent Value ${}\n".format(round(portfolio_val,3)))
		print("Worth of all assets:${}\n".format(round(funds+portfolio_val,3)))
		for item in list_:
			print("{symbol}|{num_shares}|${total}".format(**item))
		print("_____________________________")



	def quit(self):
		print("Goodbye!")

	def no_results(self):
		print("----NONE Found----")

	def sell_stock(self):
		symbol = input("SELL: Enter stock symbol:")
		num_shares = input("Enter # of shares:")
		dic = {"symbol":symbol,"num_shares":num_shares}
		return dic 

	def no_digits_error(self):
		print("-----ERROR: Contains Non Digit-----")

	def not_alpha_error(self):
		print("-----ERROR: Contains Non Letter-----")

	def invalid_amount(self):
		print("-----ERROR: INVALID INT/STOCK-----")