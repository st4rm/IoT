from gpiozero import MotionSensor
from datetime import datetime
from picamera import PiCamera


gpioin=27

pir=MotionSensor(gpioin)

camera = PiCamera()

while True:
    pir.wait_for_motion()
    print("Motion detected!")
    camera.start_preview()
    pir.wait_for_no_motion()
    camera.stop_preview()

