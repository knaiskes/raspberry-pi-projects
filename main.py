from mailSender import sendNewMail
from sensor import runSensor

while True:
	if(runSensor()):
		print("test")

