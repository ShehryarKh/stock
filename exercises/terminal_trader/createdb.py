import sqlite3 

conn = sqlite3.connect("stocks.db")

conn.execute(
	"""CREATE TABLE Users(
		id INTEGER PRIMARY KEY,
		username TEXT,
		password TEXT,
		funds INTEGER,
		permission_level INTEGER
	);	
	""")

conn.execute(
	"""CREATE TABLE Stocks(
		id INTEGER PRIMARY KEY,
		symbol TEXT,
		num_shares INTEGER,
		user_id INTEGER,
		FOREIGN KEY (user_id) REFERENCES Users(id)
	);
	""")

conn.execute(
	"""INSERT INTO Users (username, password, funds, permission_level) 
	VALUES ("Robert","123",100000,1);
	""")

conn.execute(
	"""INSERT INTO Users(username,password, funds, permission_level) 
	VALUES ("jason", "12345", 100000, 0);
	""")

conn.execute(
	"""INSERT INTO Users(username,password, funds, permission_level) 
	VALUES ("jeff", "12345", 100000, 0);
	"""
	)

conn.commit()
conn.close()
				
print("db and seed")