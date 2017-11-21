## Motion Sensor Control Code

import RPi.GPIO as GPIO
import time

gpioin=27
gpioout=22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpioin, GPIO.IN)	# Read output from Motion sensor
GPIO.setup(gpioout, GPIO.OUT) # LED output pin

while True:
	i=GPIO.input(gpioin)
        if i==0:  # When Output from motion sensor is LOW
		print "Motion sensor is not detected anything",i
		GPIO.output(gpioout, 0)	#Turn OFF LED
		time.sleep(0.1)
        elif i==1: # When Output from motion sensor is LOW
		print "Motion sensor is detected something",i
		GPIO.output(gpioout,1)	#Trun ON LED
		time.sleep(0.1)

		
