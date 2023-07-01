from __future__ import print_function
import qwiic_ccs811
import time
import sys

mySensor = qwiic_ccs811.QwiicCcs811()
mySensor.begin()
humidityVariable     = 50.0
temperatureVariable  = 22.0
mySensor.set_environmental_data(humidityVariable, temperatureVariable)

def getCO2():
	mySensor.read_algorithm_results()
	return mySensor.CO2

def getTVOC():
	mySensor.read_algorithm_results()
	return mySensor.TVOC

def runExample():

	print("\nSparkFun CCS811 Sensor Basic Example \n")

	if mySensor.connected == False:
		print("The Qwiic CCS811 device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return


	i=3
	#while True:
	while i>0:
		i= i-1
		mySensor.read_algorithm_results()

		print("CO2:\t%.3f" % mySensor.CO2)

		print("tVOC:\t%.3f\n" % mySensor.TVOC)	

		#mySensor.setEnvironmentalData(25.0, 25.0)
		humidityVariable = 25.0   # 0 to 100%
		temperatureVariable = 25.1 #5C to 70C

		print("New humidity and temperature:")
		print("  Temperature: %.2f degrees C" % temperatureVariable)
		print("  Humidity:    %.2f percent relative" % humidityVariable)

		mySensor.set_environmental_data(humidityVariable, temperatureVariable)
		
		time.sleep(1)

def setTemp(temp):
	temperatureVariable  =temp
	mySensor.set_environmental_data(humidityVariable, temperatureVariable)

def setHumidity(humidity):
	humidityVariable  =humidity
	mySensor.set_environmental_data(humidityVariable, temperatureVariable)

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Basic Example")
		sys.exit(0)
