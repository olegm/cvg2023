import qwiic_micro_oled
import sys




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

runExample()

