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
