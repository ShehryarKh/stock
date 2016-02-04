import sqlite3

conn = sqlite3.connect("stockdb.db")

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
	"""CREATE TABLE Stock(
		id INTEGER PRIMARY KEY,
		name TEXT,
		symbol TEXT,
		num_shares INTEGER,
		user_id INTEGER,
		FOREIGN KEY (user_id) REFERENCES Users(id)
		);

	""")

conn.execute(
	"""INSERT INTO Users (username, password, funds, permission_level)
	Values("khan","123", 100000, 0)
	""")

conn.execute(
	"""INSERT INTO Users (username, password, funds, permission_level)
	Values("khan1","123", 150000, 1)
	""")
conn.execute(
	"""INSERT INTO Users (username, password, funds, permission_level)
	Values("khan2","123", 200000, 1)
	""")

conn.commit()
conn.close()