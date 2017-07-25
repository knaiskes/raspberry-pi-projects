#!/usr/bin/env/python3

import urllib.request
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

redLed = 17
blueLed = 18

GPIO.setup(redLed,GPIO.OUT)
GPIO.setup(blueLed,GPIO.OUT)

mySite = ""

while(True):
	if(urllib.request.urlopen(mySite).getcode() == 200):
		# site is up and running
		GPIO.output(redLed,GPIO.LOW) 
		GPIO.output(blueLed,GPIO.HIGH)

	else:
		# something wrong is going on
		GPIO.output(blueLed,GPIO.LOW)
		GPIO.output(redLed,GPIO.HIGH)



