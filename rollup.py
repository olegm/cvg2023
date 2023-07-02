import sys

import bme280
import ccs881
import ens160
import buzzer
import camera

import display

def dowork():
	sanitydict = {"checks":0,"ens160ZeroCount":0}
	#ens160.runExample()
	ens160.setTemp( bme280.getTemp())
	ens160.setHumidity( bme280.getHumidity())

	myOLED = display.init()	
	i= 25
	while i>0:
		i=i-1
		ccs881.setTemp( bme280.getTemp())
		ccs881.setHumidity( bme280.getHumidity())
		
		print ("bme280.getTemp: ", bme280.getTemp())
		print ("bme280.getHumidity: ", bme280.getHumidity())
		print ("ens160.getAQI: ", ens160.getAQI())
		print ("ens160.getTVOC: ", ens160.getTVOC())
		print ("ens160.geteCO2: ", ens160.geteCO2())
		
		
		print ("ccs881.getCO2: ", ccs881.getCO2())
		print ("ccs881.getTVOC: ", ccs881.getTVOC())
		print ("all rolled up world!")

		sanitydict.update({"ens160eCO2"     : ens160.geteCO2()     })
		sanitydict.update({"ccs881CO2"      : ccs881.getCO2()      })
		sanitydict.update({"bme280Temp"     : bme280.getTemp()     })
		sanitydict.update({"bme280Humidity" : bme280.getHumidity() })
		sanitydict.update({"ens160TVOC"     : ens160.getTVOC()     }) 
		sanitydict.update({"ccs881TVOC"     : ccs881.getTVOC()     })
		
		sanitydict = sanitycheck(sanitydict)
		if(calculate_alarm(sanitydict)):
			soundalarm()
		else:
			quietalarm()

		display.showInfo(myOLED, \
			sanitydict.get("ens160eCO2"), \
			sanitydict.get("ccs881CO2"), \
			sanitydict.get("bme280Temp"), \
			sanitydict.get("bme280Humidity"), \
			sanitydict.get("ens160TVOC"), \
			sanitydict.get("ccs881TVOC") )



def sanitycheck(sanitydict):
	newchecks = sanitydict.get("checks") + 1
	sanitydict.update({"checks" : newchecks })
	#print("we have checed ", newchecks, " times ")
	if( sanitydict.get("ens160eCO2") == 0 ):
		sanitydict.update({"ens160ZeroCount": sanitydict.get("ens160ZeroCount") +1}) 
		if( sanitydict.get("ens160ZeroCount") > 5):
			ens160.reset()
	else:
		sanitydict.update({"ens160ZeroCount":0})
	return sanitydict


def soundalarm():
	
	return 1

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
