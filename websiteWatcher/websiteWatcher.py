#!/usr/bin/env/python3

# simple script to check if my website is up and running fine or if there is
# any problem with it

import urllib.request
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

redLed = 17
greenLed = 18

GPIO.setup(redLed,GPIO.OUT)
GPIO.setup(greenLed,GPIO.OUT)

mySite = ""

while(True):
	try:

		if(urllib.request.urlopen(mySite).getcode() == 200):
			# site is up and running
			GPIO.output(redLed,GPIO.LOW) 
			GPIO.output(greenLed,GPIO.HIGH)

		else:
			# something wrong is going on
			GPIO.output(greenLed,GPIO.LOW)
			GPIO.output(redLed,GPIO.HIGH)
		sleep(50)

	except KeyboardInterrupt:
		GPIO.output(greenLed,GPIO.LOW)
		GPIO.output(redLed,GPIO.LOW)
		exit(0)
	



