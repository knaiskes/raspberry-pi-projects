from mailSender import sendNewMail
from sensor import runSensor
from os import system
from gpiozero import MotionSensor

sensor = MotionSensor(4)

while True:
	if sensor.motion_detected:
		system("sudo fswebcam -r 1280x720 --no-banner -S 20 image.jpg")
		sendNewMail()

