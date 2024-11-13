# ultrasonic_sensor.py

import RPi.GPIO as GPIO
import time
from config import SENSOR_SETTINGS

class UltrasonicSensor:
    def __init__(self):
        GPIO.setup(SENSOR_SETTINGS["ultrasonic"]["trig_pin"], GPIO.OUT)
        GPIO.setup(SENSOR_SETTINGS["ultrasonic"]["echo_pin"], GPIO.IN)

    def measure_distance(self):
        GPIO.output(SENSOR_SETTINGS["ultrasonic"]["trig_pin"], True)
        time.sleep(0.00001)
        GPIO.output(SENSOR_SETTINGS["ultrasonic"]["trig_pin"], False)
        
        start_time = time.time()
        while GPIO.input(SENSOR_SETTINGS["ultrasonic"]["echo_pin"]) == 0:
            start_time = time.time()
        while GPIO.input(SENSOR_SETTINGS["ultrasonic"]["echo_pin"]) == 1:
            stop_time = time.time()
        
        distance = (stop_time - start_time) * 34300 / 2
        return distance < SENSOR_SETTINGS["ultrasonic"]["distance_threshold"]

