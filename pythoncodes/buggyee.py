# import curses and GPIO
import curses
import RPi.GPIO as GPIO
import os  # added so we can shut down OK
import time  # import time module
import subprocess


# import picamera and datetime (to use in unique file naming)
from picamera import PiCamera
from datetime import datetime

# setup camera
camera = PiCamera()
camera.resolution = (1280, 720)
camera.framerate = (25)

record = 0  # set up a variable to be set to 1 when recording

# set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15,   GPIO.OUT)
GPIO.setup(29, GPIO.OUT)

def liftArm():
    for i in range(50, 90):
        subprocess.call("echo 2=" + str(i) + "/dev/servoblaster", shell = True)
        time.sleep(.05)
def lowerArm():
    for i in reserved(range(50, 90)):
        subprocess.call("echo 2=" + str(i) + "/dev/servoblaster", shell=True)
        time.sleep(.05)
# flashes LEDs when all running, and also lets camera settle
for x in range(1, 5):
    GPIO.output(29, False)
    time.sleep(0.5)
    GPIO.output(29, True)
    time.sleep(0.5)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)


try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        if char == ord('S'):  # Added for shutdown on capital S
            os.system('sudo shutdown now')  # shutdown right now!
        elif char == ord('r'):
            if record == 0:
                record = 1
                moment = datetime.now()
                GPIO.output(29, False)
                camera.start_recording(
                    '/home/pi/Videos/vid_%02d_%02d_%02d.mjpg' % (moment.hour, moment.minute, moment.second))
        elif char == ord('t'):
            if record == 1:
                record = 0
                GPIO.output(29, True)
                camera.stop_recording()
        elif char == curses.KEY_UP:
            GPIO.output(7, False)
            GPIO.output(11, True)
            GPIO.output(13, False)
            GPIO.output(15, True)
        elif char == curses.KEY_DOWN:
            GPIO.output(7, True)
            GPIO.output(11, False)
            GPIO.output(13, True)
            GPIO.output(15, False)
        elif char == curses.KEY_RIGHT:
            GPIO.output(7, True)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, True)
        elif char == curses.KEY_LEFT:
            GPIO.output(7, False)
            GPIO.output(11, True)
            GPIO.output(13, True)
            GPIO.output(15, False)
        elif char == 10:
            GPIO.output(7, False)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)
        

finally:
    # Close down curses properly, inc turn echo back on!

    curses.nocbreak();
    screen.keypad(0);
    curses.echo()
    curses.endwin()
    camera.stop_recording()
    GPIO.cleanup()


