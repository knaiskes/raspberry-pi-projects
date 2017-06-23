import imaplib
import email
from keys import *

def receiveEmail():
	account = imaplib.IMAP4_SSL("imap.gmail.com")
	account.login(user_email,passw)
	account.list() #get the list of default directories
	account.select("inbox")
	result,data = account.search(None,"ALL")
	mail = data[0]
	mail_list = mail.split()
	getMail = mail_list[-1]
	result,data = account.fetch(getMail,"(RFC822)")
	decode_mail = data[0][1]
	message = email.message_from_string(decode_mail.decode("utf-8"))
	msg = email.message_from_string(decode_mail.decode("utf-8"))
	print(message["Subject"])
