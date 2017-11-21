import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print "Setup LED pins as outputs"

GPIO.setup(22, GPIO.OUT)
GPIO.output(22, False)

GPIO.output(22, True)
time.sleep(1)

GPIO.output(22, False)

raw_input('press enter to exit program')

GPIO.cleanup()
