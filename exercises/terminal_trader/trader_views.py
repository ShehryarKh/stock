
class View:

	def start(self):
		print("welcome to Trader Stocks")


	def login(self):
		username = input("Enter username :")
		password = input("Enter password :")
		dit = {'username': username, 'password': password}
		return dit


	def invalid_accounts(self):
		print("invalid login")

	def admin_login(self):
		print("you are an admin")

	def user_login(self):
		print("welcome")

	def search_term(self):
		company= input("what is the company name :")
		return company

	def main_menu(self):
		choice = input(
"""
[1] Search Stocks
[2] View Portfolio
[3] Quit
""")
		return choice

	def print_results(self, results):
		print("we found : ")
		count = 1
		for k in results:
			print(count,k['Symbol'],k['Name'])
			count+=1

	def which_result(self):
		print("which company were you looking for")
		name = input("type the brands' symbol: ")
		return name

	def show_value(self, stock_price):
		print("""""""""""""""""""""""""""""")
		print("-----------------------------")
		for k,v in stock_price.items():
			print(k,v)
		print("-----------------------------")

	def buy_main(self):
		buy_main = input("""
			[1] Buy Stock
			[2] Main Menu
			""")
		return buy_main

	def how_many(self):
		num_stocks = int(input("How many stocks do you want to purchase?"))
		return num_stocks
		
	def display_option(self):
		buy_menu = input(
"""
[y]  I do want to purchase

[n]  Go back to main menu

"""
)
		return buy_menu

	def total_cost(self,price):
		print("thats a total of ${}".format(price))


	def insufficient_funds(self):
		print("you have insufficient funds")


	def you_bought(self,sybmol,price,num_stocks):
		print("you now own {} stock of {} valued at ${}".format(num_stocks,sybmol,price))
		

