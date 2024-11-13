# modules/ai_control/autopilot.py

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
        
