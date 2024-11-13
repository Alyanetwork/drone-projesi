# jammer_control.py

import RPi.GPIO as GPIO
import time
from config import JAMMER_PIN, JAMMER_DURATION

GPIO.setmode(GPIO.BCM)
GPIO.setup(JAMMER_PIN, GPIO.OUT)

def activate_jammer():
    GPIO.output(JAMMER_PIN, GPIO.HIGH)
    time.sleep(JAMMER_DURATION)
    GPIO.output(JAMMER_PIN, GPIO.LOW)
