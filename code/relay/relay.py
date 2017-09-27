#!/usr/bin/python3

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relay_Pin = 17 

GPIO.setup(relay_Pin,GPIO.OUT)

def relayOn():
	GPIO.output(relay_Pin, GPIO.LOW)

def relayOff():
	GPIO.output(relay_Pin, GPIO.HIGH)



