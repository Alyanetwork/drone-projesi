# src/main.py

from dronekit import connect, VehicleMode
from modules.ai_control.autopilot import AutoPilot
from modules.ai_control.signal_analysis import SignalAnalysis
from modules.ai_control.behavior_analysis import BehaviorAnalysis
from modules.camera.face_recognition import FaceRecognition
from modules.camera.thermal_imaging import ThermalImaging
from modules.camera.recording import Recording
from modules.communication.satellite_comms import SatelliteComms
from modules.communication.secure_comm import SecureComm
from modules.mapping.mapping_3d import Mapping3D
from modules.security.blockchain_security import BlockchainSecurity
from modules.security.encryption import Encryption
from modules.security.jammer_control import JammerControl
from modules.sensors.ultrasonic_sensor import UltrasonicSensor
from modules.sensors.audio_processing import AudioProcessing
from modules.power.battery_management import BatteryManagement
from modules.power.solar_power import SolarPower
from config import DRONE_CONNECTION_STRING, AES_KEY

def main():
    # 1. Drone Bağlantısını Başlat
    vehicle = connect(DRONE_CONNECTION_STRING, wait_ready=True)
    vehicle.mode = VehicleMode("GUIDED")
    print("Drone bağlantısı kuruldu ve GUIDED moda alındı.")

    # 2. Modüllerin Başlatılması
    autopilot = AutoPilot(vehicle)
    signal_analysis = SignalAnalysis()
    behavior_analysis = BehaviorAnalysis()
    face_recognition = FaceRecognition()
    thermal_imaging = ThermalImaging()
    secure_comm = SecureComm(AES_KEY)
    satellite_comms = SatelliteComms()
    mapping = Mapping3D()
    blockchain = BlockchainSecurity()
    encryption = Encryption()
    jammer = JammerControl()
    ultrasonic_sensor = UltrasonicSensor()
    audio_processing = AudioProcessing()
    battery_manager = BatteryManagement()
    solar_power = SolarPower()

    # 3. Otonom Uçuş Başlatma ve GPS Rotası
    print("Otonom uçuş başlatılıyor...")
    autopilot.start_autopilot()

    # 4. Uydu Bağlantısı ve Veri Gönderimi
    satellite_comms.connect_to_satellite()
    satellite_comms.send_data("Görev verisi")
    satellite_comms.disconnect()

    # 5. 3D Haritalama ve Çevresel Tarama
    mapping.capture_environment()
    print("3D harita verileri toplandı.")

    # 6. Sinyal Analizi ve Karşı Tedbirler
    print("Sinyal analizi yapılıyor...")
    signal_analysis.analyze_signal()

    # 7. Termal Görüntüleme ile Yüz Tanıma ve Tehdit Algılama
    print("Termal görüntüleme başlatılıyor...")
    frame = thermal_imaging.capture_thermal_image()
    recognized_face = face_recognition.recognize_face(frame)
    if recognized_face == "Bilinmeyen":
        print("Tehdit durumu: Bilinmeyen kişi tespit edildi.")
        secure_comm.send_secure_message("Bölgeye bilinmeyen kişi girdi.")
    else:
        print(f"{recognized_face} tespit edildi ve kaydedildi.")
    
    # 8. Ses Tanıma ve Tehdit Durumu
    print("Ses tanıma işlemi başlatılıyor...")
    threat_status = audio_processing.listen_for_threats()
    print(f"Tehdit durumu: {threat_status}")

    # 9. Sivil/Terörist Ayrımı ve Davranış Analizi
    print("Sivil ve terörist ayrımı yapılıyor...")
    threat_level = behavior_analysis.detect_threat_level(["silah"])
    print(f"Tehdit seviyesi: {threat_level}")

    # 10. Engel Algılama ve Kaçınma
    if ultrasonic_sensor.measure_distance():
        print("Engel algılandı, rota güncelleniyor...")
        autopilot.route_planning.update_route(avoid_obstacle=True)

    # 11. Tehdit Algılama ve Jammer Aktivasyonu
    print("Tehdit algılama başlatılıyor...")
    threats = autopilot.threat_detection.identify_threats()
    if threats:
        print("Tehdit tespit edildi! Jammer aktif ediliyor.")
        jammer.activate()

    # 12. Batarya Yönetimi ve Güneş Enerjisi Şarjı
    battery_manager.monitor_battery()
    solar_power.activate_solar_charging()

    # 13. Veri Şifreleme ve Blockchain Güvenliği
    message = "Görev tamamlandı"
    encrypted_msg = encryption.encrypt_message(message)
    print(f"Şifrelenmiş mesaj: {encrypted_msg}")
    
    blockchain.create_block(message)
    blockchain.verify_chain()

    # 14. Drone Bağlantısını Kapatma
    vehicle.close()
    print("Drone bağlantısı kapatıldı.")

if __name__ == "__main__":
    main()
