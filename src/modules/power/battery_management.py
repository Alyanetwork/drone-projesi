# battery_management.py

class BatteryManagement:
    def __init__(self):
        self.battery_level = 100

    def monitor_battery(self):
        print(f"Batarya seviyesi: {self.battery_level}%")
        if self.battery_level < 20:
            print("Düşük batarya uyarısı! Şarj gereklidir.")
        self.battery_level -= 10  # Batarya tüketim simülasyonu

    def recharge_battery(self):
        print("Batarya şarj ediliyor...")
        self.battery_level = 100
        print("Batarya tamamen doldu.")
