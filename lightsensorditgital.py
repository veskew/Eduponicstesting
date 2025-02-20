"""
light sensor code 

raspi only reads digital so this inly prints 1 and 0 

vcc = 3.3v = pin 1
gnd = gnd = pin 4
do = gpio 4 = pin 7
"""

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
for i in range(0, 5):
    print(GPIO.input(4))
    time.sleep(2)
