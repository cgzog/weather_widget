# from weather_api import get_weather_forecast


import time
import RPi.GPIO as GPIO
import datetime as datetime


import servos		# gpio related stuff for servos and button
import mapping		# labels to logical servo positions
import weather		# current weather from REST polling



try:

#	servos.init()

	weather.startWeatherPolling()

	currentTimePos = mapping.labelToPos("Now")

	print("Current Time Position = ", currentTimePos)

	while 1:


		for i in mapping.getPositions().keys():

			print("Setting weather position for \"", i, "\" to ", servos.labelToAngle(i), " degrees")
			servos.setWeatherPosition(i)

			time.sleep(3)

except KeyboardInterrupt:

	servos.cleanup()




