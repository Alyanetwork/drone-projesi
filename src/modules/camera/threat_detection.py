# threat_detection.py

import cv2
from modules.camera.camera_control import CameraControl

class ThreatDetection:
    def __init__(self):
        self.camera = CameraControl()

    def identify_threats(self):
        frame = self.camera.capture_frame()
        detections = self.camera.detect_objects(frame)
        
        threats = []
        for detection in detections:
            for obj in detection:
                confidence = obj[5]
                if confidence > 0.5:
                    threats.append((obj[0], obj[1]))
        return threats
