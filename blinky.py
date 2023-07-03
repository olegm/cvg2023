import sys
import time
import RPi.GPIO as GPIO


leds = [14, 15, 18]

def dowork():
	init()
	sanitydict = {"cycle":0}
	#i= 250
	#while i>0:
	#	#i=i-1
	#	#sanitydict = soundalarm(sanitydict)
	#	sanitydict = alarm2(sanitydict)

	#	#print ("blinky world!")
	#	time.sleep(.03)
	i= 250
	while i>0:
		i = i+1
		soundalarm(3)
		quietalarm()
		time.sleep(3)

def init():
	#GPIO.setmode(GPIO.BOARD)
	GPIO.setmode(GPIO.BCM)
	for led in leds:
		GPIO.setup(led, GPIO.OUT)


def old1soundalarm(sanitydict):
	print ("                                       alarm!")

	cycle = sanitydict.get("cycle")

	if(cycle >=6 ):
		cycle = 0
	i= cycle % 2

	for led in leds :
		if(i):
			#print(led, " is on ")
			GPIO.output(led, GPIO.HIGH)
			i = 0
		else:
			#print(led, " is off ")
			GPIO.output(led, GPIO.LOW)
			i=1


	cycle += 1
	sanitydict.update({"cycle":cycle})
	return sanitydict

def alarm2(sanitydict):
	cycle = sanitydict.get("cycle") % 6

	#if(cycle >= 6 ):
	#	cycle = 0
	i = cycle % 3
	onoff = GPIO.HIGH
	if(cycle >= 3 ):
		onoff = GPIO.LOW
	led = leds[i]
	#print(led, " [",i,"]  is switching ")
	GPIO.output(led, onoff)

	cycle = cycle+1
	sanitydict.update({"cycle":cycle})
	return sanitydict
	

def soundalarm(numSeconds,sanitydict):
	sanitydict.update({"cycle":0})
	delay = .03
	while(numSeconds > 0):
		sanitydict = alarm2(sanitydict)
		numSeconds = numSeconds - delay
		time.sleep(delay)
	return sanitydict

def quietalarm():
	for led in leds:
		GPIO.output(led, GPIO.LOW)
	return 

if __name__ == '__main__':
	try:
		dowork()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Basic Example")
		sys.exit(0)
