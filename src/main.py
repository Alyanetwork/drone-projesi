# main.py

from dronekit import connect, VehicleMode
from modules.ai_control.autopilot import AutoPilot
from config import DRONE_CONNECTION_STRING

def main():
    # Drone bağlantısı
    vehicle = connect(DRONE_CONNECTION_STRING, wait_ready=True)
    vehicle.mode = VehicleMode("GUIDED")

    # Otonom kontrol modunu başlat
    autopilot = AutoPilot(vehicle)
    autopilot.start_autopilot()

    vehicle.close()

if __name__ == "__main__":
    main()
src/modules/ai_control/autopilot.py
Otonom uçuş modunu başlatan sınıf. Engel algılama, tehdit tespiti ve otomatik rota güncellemelerini içerir.

python
Kodu kopyala
# autopilot.py

from modules.sensors.ultrasonic_sensor import UltrasonicSensor
from modules.camera.threat_detection import ThreatDetection
from modules.gps.gps_navigation import GPSNavigation
from modules.security.jammer_control import JammerControl
from modules.ai_control.route_planning import RoutePlanning
from dronekit import VehicleMode

class AutoPilot:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.ultrasonic_sensor = UltrasonicSensor()
        self.threat_detection = ThreatDetection()
        self.gps_navigation = GPSNavigation(vehicle)
        self.jammer = JammerControl()
        self.route_planning = RoutePlanning()

    def start_autopilot(self):
        self.vehicle.mode = VehicleMode("GUIDED")
        print("Otonom Mod Başlatıldı.")
        
        # Görev başlat
        for waypoint in self.route_planning.get_dynamic_route():
            self.gps_navigation.goto_location(waypoint["latitude"], waypoint["longitude"], waypoint["altitude"])
            if self.ultrasonic_sensor.measure_distance():
                print("Engel Algılandı! Yeni Rota Planlanıyor...")
                self.route_planning.update_route(avoid_obstacle=True)
            
            threats = self.threat_detection.identify_threats()
            if threats:
                print("Tehdit Algılandı! Jammer Aktif.")
                self.jammer.activate()

        print("Otonom Mod Görevi Tamamlandı.")
src/modules/ai_control/route_planning.py
Dinamik rota planlama sınıfı. Engel algılamaya göre rotayı günceller.

python
Kodu kopyala
# route_planning.py

from config import WAYPOINTS

class RoutePlanning:
    def __init__(self):
        self.route = WAYPOINTS

    def get_dynamic_route(self):
        print("Dinamik Rota Oluşturuluyor...")
        return self.route

    def update_route(self, avoid_obstacle=False):
        if avoid_obstacle:
            print("Engellerden Kaçınmak İçin Yeni Rota Belirleniyor...")
            self.route = self.generate_alternative_route()
    
    def generate_alternative_route(self):
        print("Alternatif Rota Hesaplanıyor...")
        return [{"latitude": 40.714276, "longitude": -74.006000, "altitude": 20}]
src/modules/camera/camera_control.py
Kamera kontrolü ve nesne algılama için görüntü işleme sınıfı.

python
Kodu kopyala
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
src/modules/camera/threat_detection.py
Kameradan gelen görüntülerde tehdit algılama.

python
Kodu kopyala
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
src/modules/gps/gps_navigation.py
GPS ile otonom uçuş sınıfı.

python
Kodu kopyala
# gps_navigation.py

from dronekit import LocationGlobalRelative
from config import WAYPOINTS

class GPSNavigation:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def goto_location(self, latitude, longitude, altitude):
        target_location = LocationGlobalRelative(latitude, longitude, altitude)
        self.vehicle.simple_goto(target_location)

    def execute_mission(self):
        for waypoint in WAYPOINTS:
            self.goto_location(waypoint["latitude"], waypoint["longitude"], waypoint["altitude"])
src/modules/security/encryption.py
AES şifreleme ve çözme sınıfı.

python
Kodu kopyala
# encryption.py

from Crypto.Cipher import AES
import base64
from config import AES_KEY

class Encryption:
    @staticmethod
    def encrypt_message(message):
        cipher = AES.new(AES_KEY, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
        return base64.b64encode(nonce + ciphertext).decode('utf-8')

    @staticmethod
    def decrypt_message(ciphertext):
        data = base64.b64decode(ciphertext)
        nonce = data[:16]
        ciphertext = data[16:]
        cipher = AES.new(AES_KEY, AES.MODE_EAX, nonce=nonce)
        return cipher.decrypt(ciphertext).decode('utf-8')
src/modules/security/jammer_control.py
Sinyal bozucu kontrol sınıfı.

python
Kodu kopyala
# jammer_control.py

import RPi.GPIO as GPIO
import time
from config import








