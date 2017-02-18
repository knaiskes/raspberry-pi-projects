from mailSender import sendNewMail
from os import system
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.IN)
#sensor = GPIO.input(4)

print("Started")
while True:
	i = GPIO.input(4)
	if(i == 1):
		# droping 20 pixels
		system("sudo fswebcam -r 1280x720 --no-banner -S 20 image.jpg")
		sendNewMail()
		print(15 * "-")
		sleep(30) # half minute delay

