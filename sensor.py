from gpiozero import MotionSensor

def runSensor():
	pinNum = 10
	sensor = MotionSensor(pinNum)
	while True:
		if pir.motion_detected:
			return True
		else:
			return False
