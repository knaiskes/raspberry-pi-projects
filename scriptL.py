from gpiozero import LED
from time import sleep

#There are connected leds to all gpio pins that are available

ledList = [LED(4),LED(17),LED(18),LED(27),LED(22),LED(23),LED(24),LED(25)]

while True:
	for i in ledList:
		i.on()
		sleep(2)
		i.off()

