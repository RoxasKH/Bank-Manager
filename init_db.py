import sqlite3

DB_PATH = 'database.db'

connection = sqlite3.connect(DB_PATH)
with open('crea_accounts.sql') as f:
	connection.executescript(f.read())
connection.commit()
connection.close()