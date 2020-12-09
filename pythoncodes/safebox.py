import RPi.GPIO as GPIO

from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1280, 720)
camera.framerate = (25)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
