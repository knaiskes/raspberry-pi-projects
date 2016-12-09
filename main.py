from datetime import datetime
from mailSender import sendNewMail
from sensor import runSensor

currentTime = datetime.now().time()
currentTime = currentTime.replace(microsecond = 0)

