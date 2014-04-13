from math import sqrt
from colorfinder import colorz

def getCoordinates(color):
	red = int(color[1:3], 16)
	green = int(color[3:5], 16)
	blue = int(color[5:7], 16)
	return (red, green, blue)

def getColor(coordDec):
	family = (1000, 1000, 1000)
	colors = 	[(255, 0, 0),
				(0, 255, 0),
				(0, 0, 255),
				(255, 255, 0),
				(0, 255, 255),
				(255, 0, 255),
				(255, 128, 0),
				(128, 255, 0),
				(0, 255, 128),
				(0, 128, 255),
				(128, 0, 255),
				(255, 0, 128)]
	for cVal in colors:
		if getDistance(cVal, coordDec) < getDistance(family, coordDec):
			family = cVal
	black = (0, 0, 0)
	white = (255, 255, 255)
	if getDistance(white, coordDec) < 30:
		family = white
	if getDistance(black, coordDec) < 30:
		family = black
	return family

def getFamily(coordDec):
	coords = getColor(coordDec)
	if coords == (255, 0, 0):
		family = "red"
	elif coords == (0, 255, 0): 
		family = "green"
	elif coords == (0, 0, 255): 
		family = "blue"
	elif coords == (255, 255, 0): 
		family = "yellow"
	elif coords == (0, 255, 255): 
		family = "cyan"
	elif coords == (255, 0, 255): 
		family = "magenta"
	elif coords == (255, 128, 0): 
		family = "orange"
	elif coords == (128, 255, 0):
	 	family = "lime-green"
	elif coords == (0, 255, 128): 
		family = "turquiose"
	elif coords == (0, 128, 255): 
		family = "aqua"
	elif coords == (128, 0, 255): 
		family = "violet"
	elif coords == (255, 0, 128): 
		family = "pink"
	elif coords == (255, 255, 255): 
		family = "white"
	elif coords == (0, 0, 0): 
		family = "black"
	return family

def getDistance(point1, point2):
	return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 + (point1[2]-point2[2])**2)

def getMatches(coordDec):
	family = getFamily(coordDec)
	if family == "red":
		analogous = ("red", "pink", "orange")
		complementary = ("cyan", "turquiose", "aqua")
		triad = ("red", "green", "blue")
	elif family == "orange":
		analogous = ("orange", "red", "yellow")
		complementary = ("aqua", "cyan", "blue")
		triad = ("orange", "turquiose", "violet")
	elif family == "yellow":
		analogous = ("yellow", "orange", "lime-green")
		complementary = ("blue", "aqua", "violet")
		triad = ("yellow", "cyan", "magenta")
	elif family == "lime-green": 
		analogous = ("lime-green", "yellow", "green")
		complementary = ("violet", "blue", "magenta")
		triad = ("lime-green", "aqua", "pink")
	elif family == "green":
		analogous = ("green", "lime-green", "aqua")
		complementary = ("magenta", "violet", "pink")
		triad = ("red", "green", "blue")
	elif family == "turquiose":
		analogous = ("turquiose", "green", "cyan")
		complementary = ("pink", "magenta", "red")
		triad = ("orange", "turquiose", "violet")
	elif family == "cyan":
		analogous = ("cyan", "turquiose", "aqua")
		complementary = ("red", "pink", "orange")
		triad = ("yellow", "cyan", "magenta")
	elif family == "aqua":
		analogous = ("aqua", "cyan", "blue")
		complementary = ("orange", "red", "yellow")
		triad = ("lime-green", "aqua", "pink")
	elif family == "blue":
		analogous = ("blue", "aqua", "violet")
		complementary = ("yellow", "orange", "lime-green")
		triad = ("red", "green", "blue")
	elif family == "violet":
		analogous = ("lime-green", "yellow", "green")
		complementary = ("violet", "blue", "magenta")
		triad = ("orange", "turquiose", "violet")
	elif family == "magenta":
		analogous = ("magenta", "violet", "pink")
		complementary = ("green", "lime-green", "aqua")
		triad = ("yellow", "cyan", "magenta")
	elif family == "pink":
		analogous = ("pink", "magenta", "red")
		complementary = ("turquiose", "green", "cyan")
		triad = ("lime-green", "aqua", "pink")
	else:
		analogous = "grayscale"
		complementary = "pop of color" 
		triad = "mix and match"
	return (analogous, complementary, triad)

def getResults(filename):
	colorList = colorz(filename, 3)
	for c in colorList:
		test = getCoordinates(c)
		family = getFamily(test)
		if family != "white" and family != "black":
			matches = getMatches(test)
			#return "Closest color: " + str(family) + "\nAnalogous matches: " + str(matches[0]) + "\nComplementary matches: " + str(matches[1]) + "\nTriad matches: " + str(matches[2])
			return (family, matches)