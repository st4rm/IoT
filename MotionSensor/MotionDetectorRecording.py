import RPi.GPIO as GPIO
import os
from gpiozero import MotionSensor
from datetime import datetime
from picamera import PiCamera

# define motion sensor input pin
gpioin=27
# define LED out pin
gpioout=22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpioin, GPIO.IN)
GPIO.setup(gpioout, GPIO.OUT)


pir=MotionSensor(gpioin)

camera = PiCamera()

recdir = "record"  # define directory name for recording data that saved.
if not os.path.exists(recdir):
	os.makedirs(recdir)

    
while True:

    ## define filename
    now=datetime.now()
    filename = recdir
    filename += "/{0:%Y}-{0:%m}-{0:%d} {0:%H}:{0:%M}:{0:%S}".format(now)
    filename += ".h264"
    
    ## if motion is deteted, turn on LED and start recording.
    pir.wait_for_motion()
    print("Motion detected!")
    GPIO.output(gpioout, 1)
    camera.start_recording(filename)
    
    ## if motion is not detected, turn off LED and stop recording
    pir.wait_for_no_motion()
    GPIO.output(gpioout, 0)
    camera.stop_recording()

