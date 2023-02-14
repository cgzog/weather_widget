import mapping

import time
import RPi.GPIO as GPIO



#
#	setup constants for servos, button, and more
#

servoTimePin    = 18		# time servo
servoWeatherPin = 23		# weather servo
buttonPin       = 17

pwmRate         = 50


# positions are based on the evenly spaced positions around a servo on the front panel
#
# positions start at the most CW position and go CCW in even steps

servoSweep     = 180	# degrees of servo movement
numOfPositions = 6	# total number of positions for each servo

positionStep   = servoSweep / (numOfPositions - 1)	# position "0" is a position so we have one less non-zero positions




GPIO.cleanup()

GPIO.setmode(GPIO.BCM)		# Use GPIO Pins rather than board-oriented pins

GPIO.setup(servoTimePin, GPIO.OUT)
GPIO.setup(servoWeatherPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

servoTime    = GPIO.PWM(servoTimePin, pwmRate) # Setup at a 50Hz rate for the servoe - 20ms cycle
servoWeather = GPIO.PWM(servoWeatherPin, pwmRate)

servoTime.ChangeDutyCycle(10)	# start pointing full right
servoWeather.ChangeDutyCycle(10)

time.sleep(1.0)			# let things stabilize




def positionToAngle(pos):

	return pos * positionStep


def labelToPosition(label, labelDict):

	return labelDict[label]


def labelToAngle(label):

	return positionToAngle(labelToPosition(label, mapping.getPositions()))


def mapAngleToPWM(angle):

	return (angle/servoSweep) * 10 + 10		# end up between 10-20% duty cycle


def setWeatherPosition(label):

	angle = labelToAngle(label)

	print("Duty cycle set to ", mapAngleToPWM(angle), "%")
	servoWeather.ChangeDutyCycle(mapAngleToPWM(angle))


def setTimePosition(label):

	return servoTime


def cleanup():

	GPIO.cleanup()

	

def getButtonState():

	return GPIO.input(buttonPin)

