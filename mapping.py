# handle mappings from labels to positions for weather and time indications

# mapping table from conditions and time periods to the front panel display
#
# each position is a label and a logical display position since they are all evenly
# spaced across the full range of servo sweep
#
# there are two sets of indicators:  weather and time

positions = {  "Clear":        5,
               "Clouds":       4,
               "Rain":         3,
               "Thunderstorm": 2,
               "Snow":         1,
               "Mist":         0,

               "Now":          5,
               "3hr":          4,
               "6hr":          3,
               "12hr":         2,
               "24hr":         1,
               "48hr":         0
            }


def labelToPos(label):

	return positions[label]

def getPositions():

	return positions

