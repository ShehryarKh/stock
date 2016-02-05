import sqlite3

class UserDatabase:
	def __init__(self):
		self.file_name = "stocks.db"
		self.id = None 
		self.username = ''
		self.password = '' 
		self.funds = None 
		self.is_admin = None 
		self.stocks = None 
		self.symbol = ''

	def check_account(self,login):
		conn = sqlite3.connect(self.file_name)
		cursor = conn.cursor()

		cursor.execute(
			"""SELECT id,username,password,funds,permission_level 
			FROM Users 
			WHERE username = ? AND password = ?;
			""", (login["username"],login["password"]))

		row = cursor.fetchone()
		conn.commit()
		conn.close()
		if row == None:
			return False 
		self.id = row[0]
		self.username = row[1]
		self.password = row[2]
		self.funds = row[3]
		self.is_admin = row[4]
		return True

	def load_accounts(self):
		conn = sqlite3.connect(self.file_name)
		cursor = conn.cursor()

		cursor.execute(
			"""SELECT Stocks.symbol,Stocks.num_shares 
			FROM Stocks JOIN Users ON Stocks.user_id = Users.id 
			WHERE Users.username = ? AND Users.password = ?;
			""", (self.username,self.password))

		row = cursor.fetchall()
		conn.commit()
		conn.close()
		if row == None:
			return None 
		self.stocks = row  
		return row 

	def update_users(self):
		conn = sqlite3.connect(self.file_name)
		cursor = conn.cursor()

		cursor.execute(
			"""UPDATE Users 
			SET funds = ? 
			WHERE username = ? AND password = ?;
			""",(self.funds, self.username,self.password))

		conn.commit()
		conn.close()
		
	def buy_stock(self,num_shares):
		conn = sqlite3.connect(self.file_name)
		cursor = conn.cursor()

		cursor.execute(
			"SELECT id,num_shares FROM Stocks WHERE user_id = ? AND symbol = ?;",(self.id,self.symbol)
			)

		row = cursor.fetchone()
		if row == None: # if row doesn't exist
			cursor.execute(
			"INSERT INTO Stocks (symbol, num_shares, user_id) VALUES (?,?,?);",(self.symbol, num_shares, self.id)
			) #insert data above
		else:#if row exists
			id_ = row[0]
			cursor.execute(
				"UPDATE Stocks SET num_shares = ? WHERE id = ?;",(row[1]+num_shares, id_))
				#add numshares to the index row[1] which is where existing num exists
		cursor.execute(
			"UPDATE Users SET funds = ? WHERE id = ?;", (self.funds,self.id))
		#finally, insert funds minus amount bougat to update your funds 

		conn.commit()
		conn.close()

