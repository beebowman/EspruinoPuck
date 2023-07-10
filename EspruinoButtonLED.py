#Wiring instructions: 
#1) Attach 5V to the + line on breadboard
#2) Attach GND to the - line on breadboard 
#3) Connect pin 16 (GPIO 23) to the button on side A (one breadboard half)
#4) Connect the same side of button (side A) to the - of the breadboard
#5) Connect pin 12 (GPIO 18) to the longer side of the LED
#6) Connect longer (positive) side of LED to 220 Ohm resistor, on a second line of breadboard
#7) Connect the other end of resistor to - of the breadboard (GND)  


#Code is from Makeuseof.com (article on rpi buttons) 

#import RPi.GPIO library and set the board mode 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) #sets it so you use the pin numbers rather than the GPIO numbers written on it 

#declare variables for LED and button pin numbers
ledPin = 12

GPIO.setup(ledPin, GPIO.OUT) #set LED pin to output
#button pin above has been set to input and been set up with a pull-up resistor
#Using a pull-up resistor allows for clean reading from teh button,
#Since button is going to GND pin, we need a resistor to hold input pin HIGH until you press it

#Instructions:
#-check my Evernote for how to change terminal settings and determine the number referenced here for button press
#-Use Espruino bluetooth button
#-Upload RPi Puck Version 4.js code in my computer folders Fun > Programming, using the web IDE for espruino  

#import evdev
import time
from evdev import InputDevice, categorize, ecodes

#gamepad stores data 
gamepad = InputDevice('/dev/input/event9')

abutton = 48

#prints device info
print(gamepad)

start_time = time.time()
time.sleep(3) 


#pols it 
for event in gamepad.read_loop():
    end_time = time.time()
    z = end_time - start_time
    #print(z)
    if end_time - start_time > 1:
        print("Button was pressed!")
        GPIO.output(ledPin, GPIO.HIGH) #light up the LED
        time.sleep(.5)
    else:
        GPIO.output(ledPin, GPIO.LOW) #turn off LED
    start_time = time.time()
