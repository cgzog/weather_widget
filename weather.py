# make the rest call to pull the weather and maintain the state to display the weather from


# initially all set to "Clear" but will be updated once the calls are made

weather = {
		"Now": "Clear",
		"3hr": "Clear",
		"6hr": "Clear",
		"12hr": "Clear",
		"24hr": "Clear",
		"48hr": "Clear"
	  }


pollingInterval = 90 * 60		# in seconds - 90 minutes by default

weatherAvailable = False;		# goes true after first successful poll
					# reset if a poll fails

weatherLat 	= "41.4377"
weatherLong	= "-88.090417"
weatherApiKey	= "26583a6f54b1f87dc63e0a7e0b9247c0"




def startWeatherPolling():

	apiString = "https://api.openweathermap.org/data/2.5/weather?lat=" + \
                    weatherLat + "&lon=" + \
	            weatherLong + "&exclude=hourly,daily&appid=" + \
	            weatherApiKey

	print(apiString)


# def	pollNow():


# def	poll3hr():


# def	poll6hr():


# def	poll12hr():


# def	poll24r():


# def	poll48hr():
