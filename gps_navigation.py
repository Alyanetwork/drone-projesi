# gps_navigation.py

from dronekit import LocationGlobalRelative
from config import WAYPOINTS

def goto_location(vehicle, latitude, longitude, altitude):
    target_location = LocationGlobalRelative(latitude, longitude, altitude)
    vehicle.simple_goto(target_location)

def execute_mission(vehicle):
    for waypoint in WAYPOINTS:
        goto_location(vehicle, waypoint["latitude"], waypoint["longitude"], waypoint["altitude"])
