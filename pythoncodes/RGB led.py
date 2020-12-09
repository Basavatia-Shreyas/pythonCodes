import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

button1 = 16
button2 = 12
button3 = 18
button4 = 7

GPIO.setup(11,GPIO.OUT)
GPIO.output(11, 1)
GPIO.setup(13,GPIO.OUT)
GPIO.output(13, 1)
GPIO.setup(15,GPIO.OUT)
GPIO.output(15, 1)

GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button4, GPIO.IN, pull_up_down = GPIO.PUD_UP)

p = GPIO.PWM(11, 50) #red
h = GPIO.PWM(13, 50) #blue
s = GPIO.PWM(15, 50) #green



def fade():
    p.start(0)
    h.start(0)
    s.start(0)
    try:
        while True:
            for i in range(100):
                p.ChangeDutyCycle(i)
                time.sleep(.02)
            for i in range(100):
                p.ChangeDutyCycle(100-i)
                time.sleep(.02)
            for i in range(100):
                h.ChangeDutyCycle(i)
                time.sleep(.02)
            for i in range(100):
                h.ChangeDutyCycle(100-i)
                time.sleep(.02)
            for i in range(100):
                s.ChangeDutyCycle(i)
                time.sleep(.02)
            for i in range(100):
                s.ChangeDutyCycle(100-i)
                time.sleep(.02)
    except GPIO.input(button1, button2, button3, button4):
        GPIO.cleanup()
        p.stop()
        h.stop()
        s.stop()

def red():
    try:
        while True:
            p.start(0)
    except GPIO.input(button1, button2, button3, button4):
        p.stop()
        GPIO.cleanup()

def blue():
    try:
        while True:
            h.start(0)
    except GPIO.input(button1, button2, button3, button4):
        h.stop()
        GPIO.cleanup()

def green():
    try:
        while True:
            s.start(0)
    except GPIO.input(button1, button2, button3, button4):
        s.stop()
        GPIO.cleanup()

while(True):
    if GPIO.input(button1) == 0:
        fade()
    if GPIO.input(button2) == 0:
        red()
    if GPIO.input(button3) == 0:
        blue()
    if GPIO.input(button4) == 0:
        green()