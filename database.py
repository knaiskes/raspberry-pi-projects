import sqlite3
import argparse
from getpass import getpass

database = "users.db"

def main():
	parser = argparse.ArgumentParser()

	parser.add_argument("-a", "--add", action="store_true", 
			help="Add new user to the database")
	parser.add_argument("-r", "--remove", action="store_true",  
			help="Remove a user from the database")
	args = parser.parse_args()
	if args.add:
		name = input("Enter user's name: ")
		print("Enter user's password: ")
		passw = getpass()
	elif args.remove:
		user = input("Enter user's name: ")


def createDB():
	conn = sqlite3.connect(database)
	db = conn.cursor()
	db.execute("CREATE TABLE IF NOT EXISTS users (name text, password text)")
	conn.commit()
	db.close()

def addUser(name, password):
	if checkUser(name,None) == True:
		print("user: {} already exists".format(name))
	else:
		conn = sqlite3.connect(database)
		db = conn.cursor()
		db.execute("INSERT INTO users VALUES(?,?)",(name,password,))
		conn.commit()
		db.close()

def delUser(name):
	if checkUser(name,None) == True:
		conn = sqlite3.connect(database)
		db = conn.cursor()
		db.execute("DELETE FROM users VALUES(?)",(name,))
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
		db.execute("SELECT * FROM users WHERE name = ? AND password = ?",(name,password,))

	exist = db.fetchone()
	if exist is None:
		return False
	else:
		return True

	db.close()

if __name__ == "__main__":
	main()

