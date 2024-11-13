# camera_control.py

import cv2
import numpy as np
from config import CAMERA_SETTINGS

class CameraControl:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_SETTINGS["width"])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_SETTINGS["height"])
        self.cap.set(cv2.CAP_PROP_FPS, CAMERA_SETTINGS["fps"])

        self.net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        layer_names = self.net.getLayerNames()
        self.output_layers = [layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

    def capture_frame(self):
        ret, frame = self.cap.read()
        return frame if ret else None

    def detect_objects(self, frame):
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        return self.net.forward(self.output_layers)

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
