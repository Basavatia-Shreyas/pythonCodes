import RPi.GPIO as GPIO
import time
import sys
import os
from threading import Thread
from subprocess import call

GPIO.setmode(GPIO.BOARD)

button1 = 16
button2 = 12
button3 = 18
button4 = 7
button5 = 40

GPIO.setup(11,GPIO.OUT)
GPIO.output(11, 1)
GPIO.setup(13,GPIO.OUT)
GPIO.output(13, 1)
GPIO.setup(15,GPIO.OUT)
GPIO.output(15, 1)

GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

p = GPIO.PWM(11, 50) #red
h = GPIO.PWM(13, 50) #blue
s = GPIO.PWM(15, 50) #green


def restart_program():
    while(True):
        if GPIO.input(button5):
            python = sys.executable
            os.execl(python, python, * sys.argv)

def shutdown():
    if GPIO.input(button5) and GPIO.input(button1):
        call("sudo nohup shutdown -h now", shell = True)


def fade():
    p.start(0)
    h.start(0)
    s.start(0)
    try:
        while True:
            for i in range(100):
                p.ChangeDutyCycle(i)
                time.sleep(.001)
            for i in range(100):
                p.ChangeDutyCycle(100-i)
                time.sleep(.001)
            for i in range(100):
                h.ChangeDutyCycle(i)
                time.sleep(.001)
            for i in range(100):
                h.ChangeDutyCycle(100-i)
                time.sleep(.001)
            for i in range(100):
                s.ChangeDutyCycle(i)
                time.sleep(.001)
            for i in range(100):
                s.ChangeDutyCycle(100-i)
                time.sleep(.001)

    except KeyboardInterrupt:
        restart_program()
        
        
def red():
    try:
        while True:
            p.start(0)
            
    except GPIO.input():
        p.stop()
        GPIO.cleanup()

def blue():
    try:
        while True:
            h.start(0)
            
    except GPIO.input():
        h.stop()
        GPIO.cleanup()

def green():
    try:
        while True:
            s.start(0)
            
    except GPIO.input():
        s.stop()
        GPIO.cleanup()
        
def main():
    try:
    
        while(True):
                

            if GPIO.input(button1) == 1:
                fade()
            elif GPIO.input(button2) == 1:
                red()
            elif GPIO.input(button3) == 1:
                green()
            elif GPIO.input(button4) == 1:
                blue()
    except GPIO.input(button1) or GPIO.input(button2) or GPIO.input(button3) or GPIO.input(button4):
        main()
        
if __name__ == '__main__':
    Thread(target = main).start()
    Thread(target = restart_program).start()
    Thread(target = shutdown).start()
