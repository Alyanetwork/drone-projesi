# src/main.py

from dronekit import connect, VehicleMode
from modules.ai_control.autopilot import AutoPilot
from modules.ai_control.signal_analysis import SignalAnalysis
from modules.camera.thermal_imaging import ThermalImaging
from modules.communication.satellite_comms import SatelliteComms
from modules.mapping.mapping_3d import Mapping3D
from modules.security.blockchain_security import BlockchainSecurity
from modules.security.encryption import Encryption
from modules.security.jammer_control import JammerControl
from modules.sensors.ultrasonic_sensor import UltrasonicSensor
from modules.power.battery_management import BatteryManagement, SolarPower
from config import DRONE_CONNECTION_STRING

def main():
    # 1. Drone Bağlantısı
    vehicle = connect(DRONE_CONNECTION_STRING, wait_ready=True)
    vehicle.mode = VehicleMode("GUIDED")
    print("Drone bağlantısı kuruldu ve GUIDED moda alındı.")

    # 2. Modüllerin Başlatılması
    autopilot = AutoPilot(vehicle)
    signal_analysis = SignalAnalysis()
    thermal_imaging = ThermalImaging()
    satellite_comms = SatelliteComms()
    mapping = Mapping3D()
    blockchain = BlockchainSecurity()
    encryption = Encryption()
    jammer = JammerControl()
    ultrasonic_sensor = UltrasonicSensor()
    battery_manager = BatteryManagement()
    solar_power = SolarPower()

    # 3. Otonom Uçuş ve Görev Başlatma
    print("Otonom uçuş başlatılıyor...")
    autopilot.start_autopilot()

    # 4. Uydu Bağlantısı ve Veri Gönderimi
    satellite_comms.connect_to_satellite()
    satellite_comms.send_data("Görev verisi")
    satellite_comms.disconnect()

    # 5. 3D Haritalama ve Çevresel Tarama
    mapping.capture_environment()
    print("3D harita verileri toplandı.")

    # 6. Sinyal Analizi ve Karşı Tedbir
    print("Sinyal analizi yapılıyor...")
    signal_analysis.analyze_signal()

    # 7. Termal Görüntüleme ile Tehdit Algılama
    thermal_image = thermal_imaging.capture_thermal_image()
    if thermal_image is not None:
        print("Termal görüntü alındı.")

    # 8. Engel Algılama
    if ultrasonic_sensor.measure_distance():
        print("Engel algılandı, rota güncelleniyor...")
        autopilot.route_planning.update_route(avoid_obstacle=True)

    # 9. Tehdit Algılama ve Jammer Aktivasyonu
    print("Tehdit algılama başlatılıyor...")
    threats = autopilot.threat_detection.identify_threats()
    if threats:
        print("Tehdit tespit edildi! Jammer aktif ediliyor.")
        jammer.activate()

    # 10. Batarya Yönetimi ve Güneş Enerjisi Şarjı
    battery_manager.monitor_battery()
    solar_power.activate_solar_charging()

    # 11. Veri Şifreleme ve Blockchain Güvenliği
    message = "Görev tamamlandı"
    encrypted_msg = encryption.encrypt_message(message)
    print(f"Şifrelenmiş mesaj: {encrypted_msg}")
    
    blockchain.create_block(message)
    blockchain.verify_chain()

    # Drone bağlantısını kapatma
    vehicle.close()
    print("Drone bağlantısı kapatıldı.")

if __name__ == "__main__":
    main()
