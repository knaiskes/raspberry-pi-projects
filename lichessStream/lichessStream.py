#!/usr/bin/env/python3

import json
import requests
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ledPin = 17

favoriteList = [] # append the list with your favorite lichess.org streamers

keyword = "lichess.org"
client_id = "" # enter your client id
query = "https://api.twitch.tv/kraken/search/streams?query={0}/&client_id={1}".format(keyword,client_id)

GPIO.setup(ledPin,GPIO.OUT)

while(True):
	try:
		tmpList = [] 
		request = requests.get(query)
		jsonData = request.json()["streams"]

		for stream in jsonData:
			name = stream["channel"]["display_name"]
			tmpList.append(name)
		if(len(list(set(favoriteList).intersection(tmpList))) > 0):
			GPIO.output(ledPin,GPIO.HIGH)
		else:
			GPIO.output(ledPin,GPIO.LOW)
		sleep(45)
	except KeyError:
		print("There is something wrong with your client id")
		exit(0)
	except KeyboardInterrupt:
		GPIO.output(ledPin,GPIO.LOW)
		exit(0)
