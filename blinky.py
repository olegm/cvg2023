import sys
import time
import RPi.GPIO as GPIO


leds = [14, 15, 18]

def dowork():
	init()
	sanitydict = {"cycle":0}
	i= 250
	while i>0:
		#i=i-1
		sanitydict = soundalarm(sanitydict)
		print ("all rolled up world!")
		time.sleep(1)


def init():
	#GPIO.setmode(GPIO.BOARD)
	GPIO.setmode(GPIO.BCM)
	for led in leds:
		GPIO.setup(led, GPIO.OUT)


def soundalarm(sanitydict):
	print ("                                       alarm!")

	cycle = sanitydict.get("cycle")
	if(cycle == 0):
		i=0
		cycle = 1
	else:
		i=1
		cycle = 0

	for led in leds :
		if(i):
			print(led, " is on ")
			GPIO.output(led, GPIO.HIGH)
			i = 0
		else:
			print(led, " is off ")
			GPIO.output(led, GPIO.LOW)
			i=1


	#cycle += 1
	sanitydict.update({"cycle":cycle})
	return sanitydict

def quietalarm():
	return 

def calculate_alarm(sanitydict):
	return sanitydict

if __name__ == '__main__':
	try:
		dowork()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Basic Example")
		sys.exit(0)
