import sys

import bme280
import ccs881
import ens160
import buzzer
import camera

import display

def dowork():
	
	#ens160.runExample()
	ens160.setTemp( bme280.getTemp())
	ens160.setHumidity( bme280.getHumidity())

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
		display.showInfo(ens160.geteCO2(),ccs881.getCO2(),bme280.getTemp(),bme280.getHumidity(),ens160.getTVOC(), ccs881.getTVOC())

if __name__ == '__main__':
	try:
		dowork()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Basic Example")
		sys.exit(0)
