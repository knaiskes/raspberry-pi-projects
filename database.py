import sqlite3
import argparse
from getpass import getpass
import os.path
import hashlib

database = "users.db"


def main():
	parser = argparse.ArgumentParser()

	parser.add_argument("-a", "--add", action="store_true", 
			help="Add new user to the database")
	parser.add_argument("-r", "--remove", action="store_true",  
			help="Remove a user from the database")
	parser.add_argument("-u", "--users", action="store_true",
			help="List all registered users")
	args = parser.parse_args()
	if args.add:
		name = input("Enter user's name: ")
		print("Enter user's password: ")
		passw = getpass()
		addUser(name, passw)
	elif args.remove:
		user = input("Enter user's name: ")
		delUser(user)
	elif args.users:
		listUsers()


def createDB():
	conn = sqlite3.connect(database)
	db = conn.cursor()
	db.execute("""CREATE TABLE IF NOT EXISTS users 
			(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
			name TEXT NOT NULL,password Text NOT NULL)""")
	conn.commit()
	db.close()

def encryptPass(encrypt):
	password = hashlib.sha256()
	password = hashlib.sha256(encrypt.encode("utf8")).hexdigest()

	return password

def addUser(name, password):
	if checkUser(name,None) == True:
		print("user: {} already exists".format(name))
	else:
		password = encryptPass(password)
		conn = sqlite3.connect(database)
		db = conn.cursor()
		db.execute("INSERT INTO users VALUES(?,?,?)",(None,name,password,))
		conn.commit()
		db.close()

def delUser(name):
	if checkUser(name,None) == True:
		conn = sqlite3.connect(database)
		db = conn.cursor()
		db.execute("DELETE FROM users WHERE name=?",(name,))
		conn.commit()
		db.close()
	else:
		print("user: {} does not exist".format(name))

def checkUser(name, password):
	conn = sqlite3.connect(database)
	db = conn.cursor()
	if(password == None):
		db.execute("SELECT * FROM users WHERE name = ?",(name,))
	else:
		password = encryptPass(password)
		db.execute("SELECT * FROM users WHERE name = ? AND password = ?",(name,password,))

	exist = db.fetchone()
	if exist is None:
		return False
	else:
		return True

	db.close()

def listUsers():
	conn = sqlite3.connect(database)
	db = conn.cursor()
	db.execute("SELECT name FROM users")
	users = db.fetchall()
	users = " ".join(map(str,(users)))
	print("Users: ",users)
	conn.commit()
	conn.close()


if os.path.exists(database) == False:
	createDB()

if __name__ == "__main__":
	main()
