# main.py

from dronekit import connect, VehicleMode
from gps_navigation import execute_mission
from camera_control import show_camera_feed
from threat_detection import identify_threats
from jammer_control import activate_jammer
from sensor_data import check_obstacle
from security import encrypt_message, decrypt_message
from config import DRONE_CONNECTION_STRING

def main():
    # Drone bağlantısını başlat
    vehicle = connect(DRONE_CONNECTION_STRING, wait_ready=True)
    vehicle.mode = VehicleMode("GUIDED")
    
    # Kamera ve nesne algılama
    show_camera_feed()
    
    # GPS Navigasyon görevine başla
    execute_mission(vehicle)
    
    # Tehdit algılama
    frame = get_frame()  # Kamera görüntüsünü al
    threats = identify_threats(frame)
    if threats:
        print("Tehdit tespit edildi! Jammer aktif ediliyor.")
        activate_jammer()
    
    # Engel kontrolü
    if check_obstacle():
        print("Engel algılandı, yön değiştiriliyor...")
        # Engelden kaçınma algoritması eklenebilir
    
    # Verileri güvenli bir şekilde şifrele ve çöz
    message = "Örnek mesaj"
    encrypted_msg = encrypt_message(message)
    decrypted_msg = decrypt_message(encrypted_msg)
    print(f"Şifrelenmiş mesaj: {encrypted_msg}")
    print(f"Çözülmüş mesaj: {decrypted_msg}")

    vehicle.close()

if __name__ == "__main__":
    main()
