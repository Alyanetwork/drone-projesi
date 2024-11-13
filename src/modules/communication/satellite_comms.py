# src/modules/communication/satellite_comms.py

class SatelliteComms:
    def __init__(self):
        self.connected = False

    def connect_to_satellite(self):
        print("Uyduya bağlanılıyor...")
        self.connected = True
        print("Uydu bağlantısı başarılı.")

    def send_data(self, data):
        if self.connected:
            print(f"Uydu üzerinden veri gönderiliyor: {data}")
        else:
            print("Uydu bağlantısı yok, bağlantı sağlanmalı.")

    def disconnect(self):
        self.connected = False
        print("Uydu bağlantısı kesildi.")
