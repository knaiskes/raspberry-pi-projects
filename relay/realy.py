#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

lamp = 4 

GPIO.setup(lamp,GPIO.OUT)

while True:
	GPIO.output(lamp,GPIO.LOW)
	print("Lamp is on!")
	sleep(5)
	GPIO.output(lamp,GPIO.HIGH)
	print("Lamp is off!")
	sleep(5)
