# jammer_control.py

import RPi.GPIO as GPIO
import time
from config import JAMMER_SETTINGS

class JammerControl:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(JAMMER_SETTINGS["pin"], GPIO.OUT)

    def activate(self):
        GPIO.output(JAMMER_SETTINGS["pin"], GPIO.HIGH)
        time.sleep(JAMMER_SETTINGS["duration"])
        GPIO.output(JAMMER_SETTINGS["pin"], GPIO.LOW)






