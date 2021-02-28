from picamera import PiCamera
from time import sleep
from datetime import datetime
import logging
import sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

camera = PiCamera()


if __name__ == '__main__':
    try:
        camera.rotation = 180
        camera.resolution = (1920, 1080)
        camera.start_preview()
        sleep(2)  # wait 2 secs to get better image quality
        today = datetime.now()  # name the image by time
        camera.capture(f"/home/pi/{today.__str__()}")
        camera.stop_preview()
        print("Done Capturing")
        GPIO.cleanup()
    finally:
        # It is a good practice to close camera every time
        camera.close()
        print("Camera Closed")