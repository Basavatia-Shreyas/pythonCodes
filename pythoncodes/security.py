import RPi.GPIO as GPIO
import time
import os
from picamera import PiCamera
from datetime import datetime



GPIO.setmode(GPIO.BOARD)

record = 0

camera = PiCamera() #camera setup
camera.resolution = (1280, 720)
camera.framerate = (25)

button1 = 16 #six buttons on numpad
button2 = 12
button3 = 18
button4 = 7
button5 = 22
button6 = 29
vibrate = 15 #vibration sensor
servoPIN = 31 # servo

GPIO.setup(11,GPIO.OUT)

GPIO.setup(13,GPIO.OUT)


# set all the inputs and the servo
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button5, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button6, GPIO.IN, pull_up_down = GPIO.PUD_UP)

p = GPIO.PWM(servoPIN, 50) # GPIO 31 for PWM with 50Hz
p.start(7.5)  # Initialization


def secret_code():
    if GPIO.input(button1) == 0:
        if GPIO.input(button2) == 0:
            if GPIO.input(button3) == 0:
                if GPIO.input(button4) == 0:
                    if GPIO.input(button5) == 0:
                        if GPIO.input(button6) == 0:
                            p.ChangeDutyCycle(12.5)
                            time.sleep(1)
                            p.stop()


def main():
    while True:
        secret_code()