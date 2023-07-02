import time
import board
import adafruit_ens160


i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
ens = adafruit_ens160.ENS160(i2c)

def setTemp(temp):
	ens.temperature_compensation = temp

def setHumidity(humidity):
	ens.humidity_compensation = humidity

def getAQI():
    ens.read_all_sensors()
    return ens.AQI

def getTVOC():
    ens.read_all_sensors()
    return ens.TVOC

def geteCO2():
    ens.read_all_sensors()
    return ens.eCO2

def reset():
    print("         ens reset ")
    ens.reset()

def runExample():

    # Set the temperature compensation variable to the ambient temp
    # for best sensor calibration
    ens.temperature_compensation = 25
    # Same for ambient relative humidity
    ens.humidity_compensation = 50

    i = 30
    #while True:
    while i >0:
        i=i-1
        ens.read_all_sensors()
        print("AQI (1-5):", ens.AQI)
        print("TVOC (ppb):", ens.TVOC)
        print("eCO2 (ppm):", ens.eCO2)
        print()

        # new data shows up every second or so
        time.sleep(1)



if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Basic Example")
		sys.exit(0)
