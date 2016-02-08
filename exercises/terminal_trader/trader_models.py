import sqlite3

class UserDatabase:

	def __init__(self):
		self.filename = "stockdb.db"
		self.id = ''
		self.username = ''
		self.password = ''
		self.symbol = ''
		self.funds = None
		self.premission_level = 0
		self.stocks = None

	def check_account(self,login):
		conn  = sqlite3.connect(self.filename)
		cursor = conn.cursor()

		cursor.execute(
			""" SELECT id, username, password, funds, permission_level
				FROM Users
				WHERE username = ? AND password = ?;
			""",
			 (login['username'],login['password'])) 

		row = cursor.fetchone()
		conn.commit()
		conn.close()

		if row == None:
			return False
		self.id = row[0]
		self.username = row[1]
		self.password = row[2]
		self.funds = row[3]
		self.premission_level = row[4]
		return True

	def load_accounts(self):
		conn  = sqlite3.connect(self.filename)
		cursor = conn.cursor()

		cursor.execute(
			""" SELECT symbol, num_shares
				FROM Stock JOIN Users ON Stock.user_id = Users.id
				WHERE Users.username = ? AND Users.password = ?;

			""", (self.username,self.password))

		row = cursor.fetchall()
		conn.commit()
		conn.close()
		if row == None:
			return None
		self.stocks = row
		return row

	def update_users(self,remaining_funds):
		conn  = sqlite3.connect(self.filename)
		cursor = conn.cursor()
		cursor.execute(
			""" UPDATE Users SET funds = ? WHERE id = ?;""",(remaining_funds, self.id))
		conn.commit()
		conn.close()	
		
	def buy_stock(self,num_shares):
		conn  = sqlite3.connect(self.filename)
		cursor = conn.cursor()
		cursor.execute(
			""" INSERT INTO Stock(symbol,num_shares,user_id) VALUES (?,?,?);""", (self.symbol, num_shares, self.id)
			)
		conn.commit()
		conn.close()

