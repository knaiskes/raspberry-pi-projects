from gpiozero import MotionSensor

def runSensor(pinNum):
	sensor = MotionSensor(pinNum)
	while True:
		if pir.motion_detected:
			# add later
