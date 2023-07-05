# cvg2023
My build for Convergence-con 2023 #cvg2023

This uses a few I2C devices
CCS881
ENS160
BME280
Sparkfun Qwiic oled display

All the sensors were purchased from Sparkfun, but any source will do, if you are not concerned with the 3d print holding the parts together.

There are three adafruit 'noods' LED's Soldered into the GPIO pins indicated in rollup.py

To run the project, you'll probably need to install the appropriate libraries from Adafruit and Sparkfun.

Once libraries are installed 

sudo python3 rollup.py

As it inits, it will blink the lights so you know that they are working.

If the program detects co2 that is too high the LED's will flash rapidly until it is removed from the stale air environment.

There is a partymode as well, but I probably won't use that. 


