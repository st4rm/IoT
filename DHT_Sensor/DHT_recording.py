#!/usr/bin/python

import Adafruit_DHT
import time
import os
from datetime import datetime

# Sensor should be set to Adafruit_DHT.DHT11, 
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT11

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 23

recdir = "record"  # define directory name for recording data that saved.
if not os.path.exists(recdir):
	os.makedirs(recdir)

now=datetime.now()
filename = recdir
filename += "/{0:%Y}-{0:%m}-{0:%d}".format(now)
filename +=".txt"

f= open(filename, 'a')

sec=float(raw_input("Enter the priod of time(second) to recording Temperature and Humidity: "))

print('Temperature and Humidity are recording...')

while True:

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).

        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

	if humidity is not None and temperature is not None:
                now=datetime.now()
		data="{0:%Y}-{0:%m}-{0:%d} {0:%H}:{0:%M}:{0:%S}".format(now)
		data += '     Temp={0:0.1f}*C Humidity={1:0.1f}%\n'.format(temperature, humidity)
                # print(data)
		f.write(data)
	else:
		print('Failed to get reading. Try again!')
	time.sleep(sec) # write data every (sec) Seconds.

f.clolse()
