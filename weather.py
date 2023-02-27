# make the rest call to pull the weather and maintain the state to display the weather from

import requests
import json
import os
import sys
import time


# initially all set to "Clear" but will be updated once the calls are made

weather = {	# display: { condition, time }

		"Now":  [ "Clear", 12345 ],
		"3hr":  [ "Clear", 23456 ],
		"6hr":  [ "Clear", 34567 ],
		"12hr": [ "Clear", 45678 ],
		"24hr": [ "Clear", 56789 ],
		"48hr": [ "Clear", 67890 ]
	  }


pollingInterval     = 90 * 60		# in seconds - 90 minutes by default

weatherAvailable    = False;		# goes true after first successful poll
					# reset if a poll fails

weatherLat          = "41.4377"
weatherLong         = "-88.090417"
weatherApiKeyEnvVar = "OPEN_WEATHER_API_KEY"
weatherApiKey       = ""




def startWeatherPolling():

	weatherApiKey = os.environ[weatherApiKeyEnvVar]

	if (len(weatherApiKey) == 0):
		print(sys.argv[0] + ": error: OPEN_WEATHER_API_KEY not set\n")
		sys.exit(1)

	pollNow(weatherApiKey)

	pollFuture(weatherApiKey)



def	pollNow(apiKey):

	nowApiCall = "https://api.openweathermap.org/data/2.5/weather?lat=" + \
                       weatherLat + "&lon=" + \
	               weatherLong + "&exclude=hourly,daily&appid=" + \
	               apiKey

	# print(nowApiCall, "\n")

	response = requests.get(nowApiCall)

	if (response.status_code == 200):
		weatherAvailable = True
	else:
		weatherAvailable = False
		return
		
	weatherNow = json.loads(response.text)

	# save "now" condition and timestamp
	weather['Now'][0] = weatherNow['weather'][0]['main']
	weather['Now'][1] = weatherNow['dt']

	print("weather['Now'] ", weather['Now'], end = "\n\n")



def	pollFuture(apiKey):

	print("pollFuture(): apiKey = ", apiKey, end="\n")

	now = int(time.time())

	print("now = ", now, end="\n")

	futureApiCall = "https://api.openweathermap.org/data/2.5/forecast?lat=" + \
                        weatherLat + "&lon=" + \
	                weatherLong + "&exclude=hourly,daily&appid=" + \
	                apiKey

	# print(futureApiCall, "\n")

	response = requests.get(futureApiCall)

	if (response.status_code == 200):
		weatherAvailable = True
	else:
		weatherAvailable = False
		return
		

	print(response.json(), "\n")

	weatherForecast = json.loads(response.text)

	print(type(weatherForecast), "cnt = ", weatherForecast['cnt'], end="\n")

	jsonPrettyPrint = json.dumps(weatherForecast, indent=4)
	print(jsonPrettyPrint)
