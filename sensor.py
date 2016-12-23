from gpiozero import MotionSensor

def runSensor():
	pinNum = 4
	sensor = MotionSensor(pinNum)
	while True:
		if sensor.motion_detected:
			return True
		else:
			return False
