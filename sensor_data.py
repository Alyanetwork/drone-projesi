# sensor_data.py

import RPi.GPIO as GPIO
import time
from config import ULTRASONIC_TRIG, ULTRASONIC_ECHO, DISTANCE_THRESHOLD

GPIO.setup(ULTRASONIC_TRIG, GPIO.OUT)
GPIO.setup(ULTRASONIC_ECHO, GPIO.IN)

def measure_distance():
    GPIO.output(ULTRASONIC_TRIG, True)
    time.sleep(0.00001)
    GPIO.output(ULTRASONIC_TRIG, False)
    start_time = time.time()
    while GPIO.input(ULTRASONIC_ECHO) == 0:
        start_time = time.time()
    while GPIO.input(ULTRASONIC_ECHO) == 1:
        stop_time = time.time()
    distance = (stop_time - start_time) * 34300 / 2
    return distance

def check_obstacle():
    return measure_distance() < DISTANCE_THRESHOLD
