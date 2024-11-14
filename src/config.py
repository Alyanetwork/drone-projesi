# src/config.py

# Drone bağlantı ayarları
DRONE_CONNECTION_STRING = '127.0.0.1:14550'

# Kamera ayarları
CAMERA_SETTINGS = {
    "width": 640,
    "height": 480,
    "fps": 30
}

# GPS rotaları (waypoints)
WAYPOINTS = [
    {"latitude": 40.712776, "longitude": -74.005974, "altitude": 20},
    {"latitude": 40.713776, "longitude": -74.006974, "altitude": 25}
]

# AES Şifreleme Anahtarı (kriptolu iletişim ve veri güvenliği için)
AES_KEY = b'Sixteen byte key'

# Jammer (sinyal bozucu) ayarları
JAMMER_SETTINGS = {
    "pin": 18,           # GPIO pin numarası
    "duration": 10       # Aktif kalma süresi (saniye)
}

# Sensör ayarları
SENSOR_SETTINGS = {
    "ultrasonic": {
        "trig_pin": 23,      # Ultrasonik sensör tetikleme pini
        "echo_pin": 24,      # Ultrasonik sensör yankı pini
        "distance_threshold": 50  # Engel algılama mesafesi (cm)
    },
    "lidar": {
        "port": "/dev/ttyUSB0",   # Lidar bağlantı noktası
        "baudrate": 115200        # Lidar baudrate
    }
}

# Yüz tanıma ayarları
FACE_RECOGNITION_SETTINGS = {
    "database_path": "face_database",    # Yüz veritabanı kayıt yeri
    "unknown_label": "Bilinmeyen"        # Bilinmeyen yüzler için etiket
}

# Ses tanıma ayarları
AUDIO_RECOGNITION_SETTINGS = {
    "language": "tr-TR",  # Ses tanıma dili
    "threat_keywords": ["yardım", "tehdit"]  # Tehdit kelimeleri
}

# Termal kamera ayarları (opsiyonel)
THERMAL_CAMERA_SETTINGS = {
    "device_index": 0     # Termal kamera cihaz indeksi
}

# Kriptolu iletişim ayarları
SECURE_COMM_SETTINGS = {
    "control_center_url": "https://control-center.example.com/api",  # En yakın kontrol merkezi URL'si
    "auth_token": "YOUR_SECURE_AUTH_TOKEN"  # Kontrol merkezi ile iletişim için güvenlik anahtarı
}

# Blockchain tabanlı güvenlik ayarları
BLOCKCHAIN_SETTINGS = {
    "blockchain_node": "https://blockchain.example.com",  # Blockchain düğüm adresi
    "chain_id": "drone_security_chain"  # Blockchain zincir adı
}

# Batarya ve güç yönetimi ayarları
BATTERY_SETTINGS = {
    "low_battery_threshold": 20,  # Düşük batarya uyarı seviyesi (%)
    "solar_charge_enabled": True  # Güneş enerjisi ile şarj seçeneği
}

# Uydu tabanlı iletişim ayarları
SATELLITE_COMM_SETTINGS = {
    "connection_timeout": 5,  # Uydu bağlantı süresi (saniye)
    "satellite_url": "https://satellite.example.com"  # Uydu iletişim URL'si
}
