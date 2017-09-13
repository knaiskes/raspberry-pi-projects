import sqlite3

conn = sqlite3.connect("users.db")

db = conn.cursor()


def createDB():
	db.execute("CREATE TABLE IF NOT EXISTS users (name text, password text)")

def addUser():
	db.execute("INSERT INTO users VALUES('','')")


def checkUser(name, password):
	db.execute("SELECT * FROM users WHERE name = ? AND password = ?",(name,password,))
	exist = db.fetchone()
	if exist is None:
		print("does not exist")
	else:
		print("Exists")
	
createDB()
addUser()
checkUser("","")

conn.commit()
conn.close()
