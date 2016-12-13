from mailSender import sendNewMail
from sensor import runSensor
from os import system

while True:
	if(runSensor()):
		system("sudo fswebcam -r 1280x720 --no-banner image.jpg")
		sendNewMail()

