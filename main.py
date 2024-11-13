# main.py

from dronekit import connect, VehicleMode
from modules.gps.gps_navigation import GPSNavigation
from modules.camera.threat_detection import ThreatDetection
from modules.security.jammer_control import JammerControl
from modules.security.encryption import Encryption
from modules.sensors.ultrasonic_sensor import UltrasonicSensor
from config import DRONE_CONNECTION_STRING

def main():
    # Drone bağlantısı
    vehicle = connect(DRONE_CONNECTION_STRING, wait_ready=True)
    vehicle.mode = VehicleMode("GUIDED")

    # Modülleri başlat
    gps_navigation = GPSNavigation(vehicle)
    threat_detection = ThreatDetection()
    jammer = JammerControl()
    encryption = Encryption()
    ultrasonic_sensor = UltrasonicSensor()

    # Görev ve uçuş başlatma
    gps_navigation.execute_mission()

    # Tehdit algılama ve jammer aktivasyonu
    threats = threat_detection.identify_threats()
    if threats:
        print("Tehdit tespit edildi! Jammer aktif.")
        jammer.activate()

    # Engel kontrolü
    if ultrasonic_sensor.measure_distance():
        print("Engel tespit edildi, yön değiştiriliyor...")

    # Veri şifreleme ve çözme örneği
    message = "Örnek mesaj"
    encrypted_msg = encryption.encrypt_message(message)
    decrypted_msg = encryption.decrypt_message(encrypted_msg)
    print(f"Şifreli mesaj: {encrypted_msg}")
    print(f"Çözülen mesaj: {decrypted_msg}")

    vehicle.close()

if __name__ == "__main__":
    main()
