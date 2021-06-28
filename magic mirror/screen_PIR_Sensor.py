import RPi.GPIO as GPIO
import time
import sys
from subprocess import run

#time stamp
def get_timestamp():
    t = time.localtime()
    return time.strftime("%H:%M:%S", t)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
try:
    while True:
        i = GPIO.input(4)
        if i ==0:
            print("Screen off", i)
            run("vcgencmd display_power 0", shell = True)
            print(get_timestamp())
            time.sleep(1)
        elif i ==1:
            print("Screen on", i)
            run("vcgencmd display_power 1", shell = True)
            print(get_timestamp())
            time.sleep(25)

except KeyboardInterrupt:
    run("vcgencmd display_power 1", shell = True)
