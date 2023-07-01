import qwiic_micro_oled
import sys
import time

def runExample():

    #  These three lines of code are all you need to initialize the
    #  OLED and print the splash screen.
  
    #  Before you can start using the OLED, call begin() to init
    #  all of the pins and configure the OLED.


    #print("\nSparkFun Micro OLED - Hello Example\n")
    myOLED = qwiic_micro_oled.QwiicMicroOled()

    #if False:  #myOLED.isConnected() == False:
    if not myOLED.connected:
        #print("The Qwiic Micro OLED device isn't connected to the system. Please check your connection", \
            #file=sys.stderr)
        return

    #  Before you can start using the OLED, call begin() to init all of the pins and configure the OLED.
    myOLED.begin()
    myOLED.clear(myOLED.PAGE)  #  Clear the display's buffer
    myOLED.print("Hello World")  #  Add "Hello World" to buffer

    #  To actually draw anything on the display, you must call the display() function. 
    myOLED.display()

def init():
    myOLED = qwiic_micro_oled.QwiicMicroOled()
    if not myOLED.connected:
        print("The Qwiic Micro OLED device isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    #myOLED.begin()
    myOLED.begin()
    return myOLED

def showInfo(myOLED,ens, ccs,temp,hum,Evoc, Cvoc):
    print ("ens: ", ens, " ccs: ", ccs)

    #myOLED = qwiic_micro_oled.QwiicMicroOled()

    #if False:  #myOLED.isConnected() == False:

    #myOLED.clear(myOLED.PAGE)  #  Clear the display's buffer
    myOLED.begin()

    myOLED.print("ens: % 5d" % ens)
    myOLED.print("ccs: % 5d" % ccs)
    myOLED.print("temp: % 3dc" % temp)
    myOLED.print("hum:  % 3d" % hum)
    myOLED.print("%")
    myOLED.print("voc1: % 4d" % Evoc)
    myOLED.print("voc2: % 4d" % Cvoc)

    myOLED.display()


if __name__ == '__main__':
    try:
        myOLED = init()
        print ("before")
        showInfo(myOLED, 1,2,3,4,5,6)
        print ("after")
        time.sleep(1)
        showInfo(myOLED, 6,5,4,3,2,1)
        print ("after")
        #runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Basic Example")
        sys.exit(0)

