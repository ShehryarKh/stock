import sqlite3
from trader_views import View
from trader_models import *

class controller():

	def __init__(self):
		self.view = View()
		self.user = UserDatabase()
		self.quit = ["quit", "q"]
		self.choice = ''

	def run (self):
		self.view.start()
		self.login_()

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
c = controller()
c.run()
