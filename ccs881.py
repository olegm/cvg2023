from __future__ import print_function
import qwiic_ccs811
import time
import sys

def runExample():

	print("\nSparkFun CCS811 Sensor Basic Example \n")
	mySensor = qwiic_ccs811.QwiicCcs811()

	if mySensor.connected == False:
		print("The Qwiic CCS811 device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	mySensor.begin()

	while True:

		mySensor.read_algorithm_results()

		print("CO2:\t%.3f" % mySensor.CO2)

		print("tVOC:\t%.3f\n" % mySensor.TVOC)	

		humidityVariable = random.randrange(0, 10000)/100   # 0 to 100%
		temperatureVariable = random.randrange(500, 7000) / 100 #5C to 70C

		print("New humidity and temperature:")
		print("  Humidity:    %.2f percent relative" % humidityVariable)
		print("  Temperature: %.2f degrees C" % temperatureVariable)

		mySensor.set_environmental_data(humidityVariable, temperatureVariable)
		
		time.sleep(1)


if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Basic Example")
		sys.exit(0)
