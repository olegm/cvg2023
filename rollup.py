import sys
import time
import RPi.GPIO as GPIO

import bme280
import ccs881
import ens160
#import buzzer
#import camera
import display
import blinky

leds = [14, 15, 18]

def dowork():
	sanitydict = {"checks":0, \
		"ens160ZeroCount":0, \
		"cycle":0, \
		"loops":0, \
		"delay":.031, \
		"etol":900, \
		"ctol":1800, \
	}

	init()
	#ens160.runExample()

	myOLED = display.init()	
	i= 250
	while i>0:
		#i=i-1
		if(sanitydict.get("loops")>10):
			ccs881.setTemp( bme280.getTemp())
			ccs881.setHumidity( bme280.getHumidity())
			ens160.setTemp( bme280.getTemp())
			ens160.setHumidity( bme280.getHumidity())
			sanitydict.update({"loops":0})

		#print ("ens160.eCO2: ", sanitydict.get("ens160eCO2") )
		#print ("ccs881.CO2: ", sanitydict.get("ccs881CO2") )
		#print ("bme280.Temp: ", sanitydict.get("bme280Temp") )
		#print ("bme280.Humidity: ", sanitydict.get("bme280Humidity") )
		#print ("ens160.TVOC: ", sanitydict.get("ens160TVOC") )
		#print ("ccs881.TVOC: ", sanitydict.get("ccs881TVOC") )


		sanitydict.update({"ens160eCO2"     : ens160.geteCO2()     })
		sanitydict.update({"ccs881CO2"      : ccs881.getCO2()      })
		sanitydict.update({"bme280Temp"     : bme280.getTemp()     })
		sanitydict.update({"bme280Humidity" : bme280.getHumidity() })
		sanitydict.update({"ens160TVOC"     : ens160.getTVOC()     }) 
		sanitydict.update({"ccs881TVOC"     : ccs881.getTVOC()     })
		
		sanitydict = sanitycheck(sanitydict)

		display.showInfo(myOLED, \
			sanitydict.get("ens160eCO2"), \
			sanitydict.get("ccs881CO2"), \
			sanitydict.get("bme280Temp"), \
			sanitydict.get("bme280Humidity"), \
			sanitydict.get("ens160TVOC"), \
			sanitydict.get("ccs881TVOC") )

		if(calculate_alarm(sanitydict)):
			if(sanitydict.get("cycle")):
				#sanitydict = blinky.alarm2(sanitydict)
				sanitydict = blinky.soundalarm(3,sanitydict)

			else:
				sanitydict = blinky.soundalarm(30,sanitydict)
		else:
			blinky.quietalarm()

		print ("all rolled up world!")
		time.sleep(1)

def sanitycheck(sanitydict):
	newchecks = sanitydict.get("checks") + 1
	sanitydict.update({"checks" : newchecks })
	#print("we have checed ", newchecks, " times ")
	if( sanitydict.get("ens160eCO2") == 0 ):
		sanitydict.update({"ens160ZeroCount": sanitydict.get("ens160ZeroCount") +1}) 
		if( sanitydict.get("ens160ZeroCount") > 5):
			ens160.reset()
			sanitydict.update({"ens160ZeroCount":0})
	else:
		sanitydict.update({"ens160ZeroCount":0})

	return sanitydict

def init():
	#GPIO.setmode(GPIO.BOARD)
	for led in leds:
		GPIO.setup(led, GPIO.OUT)
		GPIO.output(led, GPIO.HIGH)
		time.sleep(1)
	for led in leds:
		GPIO.output(led, GPIO.LOW)
		time.sleep(1)

	ens160.setTemp( bme280.getTemp())
	ens160.setHumidity( bme280.getHumidity())
	ccs881.setTemp( bme280.getTemp())
	ccs881.setHumidity( bme280.getHumidity())


def calculate_alarm(sanitydict):
	rval = 0
			
	etol = sanitydict.get("etol") #		"etol":900, \
	ctol = sanitydict.get("ctol") #		"ctol":1800, \

	eeco2 = sanitydict.get("ens160eCO2")
	#eeco2 = eeco2 - sanitydict.get("ens160TVOC")
	ceco2 = sanitydict.get("ccs881CO2")
	#ceco2 = ceco2 - sanitydict.get("ccs881TVOC")

	if(sanitydict.get("ens160eCO2") != 0):
		if(eeco2 > etol and ceco2 > ctol):
			rval = 1
	else:
		if( ceco2 > ctol):
			rval = 1

	return rval

if __name__ == '__main__':
	try:
		dowork()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding rollup")
		blinky.quietalarm()
		#display.clear(myOLED)
		sys.exit(0)
