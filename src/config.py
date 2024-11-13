# config.py

# Drone bağlantı ayarları
DRONE_CONNECTION_STRING = '127.0.0.1:14550'

# Kamera ayarları
CAMERA_SETTINGS = {
    "width": 640,
    "height": 480,
    "fps": 30
}

# GPS Koordinatları
WAYPOINTS = [
    {"latitude": 40.712776, "longitude": -74.005974, "altitude": 20},
    {"latitude": 40.713776, "longitude": -74.006974, "altitude": 25}
]

# Güvenlik ve şifreleme ayarları
AES_KEY = b'Sixteen byte key'

# Jammer ayarları
JAMMER_SETTINGS = {"pin": 18, "duration": 10}

# Sensör ayarları
SENSOR_SETTINGS = {
    "ultrasonic": {"trig_pin": 23, "echo_pin": 24, "distance_threshold": 50},
    "lidar": {"port": "/dev/ttyUSB0", "baudrate": 115200}
}
,
