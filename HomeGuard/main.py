from mailSender import sendNewMail
from subprocess import run
from time import sleep
from sys import exit
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

sensorPin = 4
GPIO.setup(sensorPin,GPIO.IN)

print("Started")

try:
	while True:
		sensor = GPIO.input(sensorPin)
		if(sensor == 1):
			try:
				# taking a screenshot and dropping 20 pixels
				# add sudo if you are not int the video group
				run("sudo fswebcam -r 1280x720 --no-banner -S 20 image.jpg",shell=True)
			except OSError:
				print("Could not start fswebcam")
			sendNewMail()
			print(15 * "-")
			sleep(30) # half a minute delay
except KeyboardInterrupt:
	exit(0)
