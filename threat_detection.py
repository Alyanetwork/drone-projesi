# threat_detection.py

import cv2
import numpy as np
from camera_control import detect_objects

def identify_threats(frame):
    threats = []
    detections = detect_objects(frame)
    for detection in detections:
        for obj in detection:
            confidence = obj[5]
            if confidence > 0.6:
                threats.append((obj[0], obj[1]))
    return threats
