from gpiozero import LED
from time import sleep
from random import randint

#funtions are tested on raspberry pi b

#There are connected leds to all gpio pins that are available

#global led list, you may want to change it or expand it if you are using
#a differet raspberry pi version 
ledList = [LED(4),LED(17),LED(18),LED(27),LED(22),LED(23),LED(24),LED(25)]

def allOnandOff(leds):
	#Turn on and off every led after 2 seconds
	while True:
		for i in leds:
			i.on()
			sleep(2)
			i.off()
def randomOnOff(leds):
	#Turn on and off random leds
	while True:
		random_led = randint(0,7)
		randomLed = ledList[random_led]
		randomLed.on()
		sleep(2)
		randomLed.off()

#uncomment the function that you want to use, make sure all others funtions be
#commented out

#allOnandOff(ledList)
randomOnOff(ledList)

