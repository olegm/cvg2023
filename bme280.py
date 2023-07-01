print ("hello world! - BME280")

import qwiic_bme280
import time
import sys
mySensor = qwiic_bme280.QwiicBme280()

def runExample():

	print("\nSparkFun BME280 Sensor  Example 1\n")

	if mySensor.connected == False:
		print("The Qwiic BME280 device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	mySensor.begin()
	i = 3
	#while True:
	while i >0:
		i=i-1
		
		print("Humidity:\t%.3f" % mySensor.humidity)

		print("Pressure:\t%.3f" % mySensor.pressure)	

		print("Altitude:\t%.3f" % mySensor.altitude_feet)

		print("Temperature:\t%.2f" % mySensor.temperature_fahrenheit)		
		print("Temperature:\t%.2f" % mySensor.temperature_celsius)		

		print("")
		
		time.sleep(1)

def getTemp():
	mySensor.begin()
	return mySensor.temperature_celsius

def getHumidity():
	mySensor.begin()
	return mySensor.humidity



if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Basic Example")
		sys.exit(0)
