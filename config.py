# config.py

# Drone bağlantı ayarları
DRONE_CONNECTION_STRING = '127.0.0.1:14550'

# Kamera ayarları
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# GPS Koordinatları
WAYPOINTS = [
    {"latitude": 40.712776, "longitude": -74.005974, "altitude": 20},  # Örnek Koordinat 1
    {"latitude": 40.713776, "longitude": -74.006974, "altitude": 25}   # Örnek Koordinat 2
]

# Güvenlik ve şifreleme anahtarları
AES_KEY = b'Sixteen byte key'  # 16 byte AES şifreleme anahtarı

# Jammer ayarları
JAMMER_PIN = 18
JAMMER_DURATION = 10  # Saniye cinsinden

# Sensör ve engel algılama
ULTRASONIC_TRIG = 23
ULTRASONIC_ECHO = 24
DISTANCE_THRESHOLD = 50  # Engel algılama mesafesi cm cinsinden
