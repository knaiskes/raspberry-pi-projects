from mailSender import sendNewMail
from os import system
from gpiozero import MotionSensor
from time import sleep

sensor = MotionSensor(4)

print("Started")
while True:
	if sensor.motion_detected:
		#droping 20 pixels
		system("sudo fswebcam -r 1280x720 --no-banner -S 20 image.jpg")
		sendNewMail()
		print(15 * "-")
		sleep(30) # half minute delay

