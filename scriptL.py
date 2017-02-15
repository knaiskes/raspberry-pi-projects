#!/usr/bin/env python

from time import sleep
from sys import exit
from random import randint
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# script has been tested on raspberry pi b
# there are leds connected to all  available gpio pins 
# global led list, you may want to change it or expand it if you are using
# a differet raspberry pi version 

ledList = [4,17,18,27,22,23,24,25]
for i in ledList:
	GPIO.setup(i,GPIO.OUT)

def testLeds(leds):
	for i in leds:
		GPIO.output(i,GPIO.HIGH)
	sleep(5)
	for i in leds:
		GPIO.output(i,GPIO.LOW)

def allOnandOff(leds):
	# turn on and off every led after 1 seconds
	# from start to end and back
	while True:
		for i in leds: 
			GPIO.output(i,GPIO.HIGH)
			sleep(2)
			GPIO.output(i,GPIO.LOW)
		for i in reversed(leds):
			GPIO.output(i,GPIO.HIGH)
			sleep(2)
			GPIO.output(i,GPIO.LOW)
def randomOnOff(leds):
	# Turn on and off random leds from the list
	while True:
		random_led = randint(0,7)
		randomLed = ledList[random_led]
		GPIO.output(randomLed,GPIO.HIGH)
		sleep(2)
		GPIO.output(randomLed,GPIO.LOW)

def allOff(leds):
	for i in leds:
		GPIO.output(i,GPIO.LOW)

try:
	testLeds(ledList)
	# allOnandOff(ledList)
	# randomOnOff(ledList)
except KeyboardInterrupt:
	allOff(ledList)
	exit(0)
