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