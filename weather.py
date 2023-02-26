# make the rest call to pull the weather and maintain the state to display the weather from

import requests
import json
import os
import sys


# initially all set to "Clear" but will be updated once the calls are made

weather = {
		"Now": "Clear",
		"3hr": "Clear",
		"6hr": "Clear",
		"12hr": "Clear",
		"24hr": "Clear",
		"48hr": "Clear"
	  }


pollingInterval     = 90 * 60		# in seconds - 90 minutes by default

weatherAvailable    = False;		# goes true after first successful poll
					# reset if a poll fails

weatherLat          = "41.4377"
weatherLong         = "-88.090417"
weatherApiKeyEnvVar = "OPEN_WEATHER_API_KEY"
weatherApiKey       = ""
#weatherApiKey      = "26583a6f54b1f87dc63e0a7e0b9247c0"




def startWeatherPolling():

	weatherApiKey= os.environ[weatherApiKeyEnvVar]
	if (len(weatherApiKey) == 0):
		print(sys.argv[0] + ": error: OPEN_WEATHER_API_KEY not set\n")
		sys.exit(1)

	apiString = "https://api.openweathermap.org/data/2.5/weather?lat=" + \
                    weatherLat + "&lon=" + \
	            weatherLong + "&exclude=hourly,daily&appid=" + \
	            weatherApiKey

	print(apiString, "\n")

	pollNow(apiString)

	poll3hr()

	poll6hr()

	poll12hr()

	poll24hr()

	poll48hr()


def	pollNow(apiString):

	response = requests.get(apiString)

	print("Ret Code = ", response.status_code, "\n")

	print(response.json(), "\n")

	weatherNow = json.loads(response.text)

	print(type(weatherNow), "coord = ", weatherNow['coord'], end="\n")
	print("lat = ", weatherNow['coord']['lat'], end="\n")
	print("now = ", weatherNow['weather'][0]['main'], end="\n")


def	poll3hr():

	print("Poll3hr()", "\n")


def	poll6hr():

	print("Poll6hr()", "\n")


def	poll12hr():

	print("Poll12hr()", "\n")


def	poll24hr():

	print("Poll24hr()", "\n")


def	poll48hr():

	print("Poll48hr()", "\n")
