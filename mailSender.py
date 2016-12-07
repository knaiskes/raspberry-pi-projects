import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from keys import * # I keep my personal information in a separate file

def sendNewMail():
	#define your personal information below or in a separate file as I did
	#user_email =""
	#passw = ""
	#sendTo = ""
	sub = "New alarm"
	image = "icon.png"
	message = MIMEMultipart()
	message["Subject"] = sub
	message["From"] = user_email
	message["To"] = sendTo
	message.premble = "alert"

	fp = open(image,"rb")
	image = MIMEImage(fp.read())
	fp.close()
	
	message.attach(image)

	sendIt = smtplib.SMTP("smtp.gmail.com",587)
	sendIt.ehlo()
	sendIt.starttls()
	sendIt.ehlo()
	sendIt.login(user_email,passw)
	sendIt.send_message(message)
	sendIt.quit()
