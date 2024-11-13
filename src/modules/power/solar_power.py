# solar_power.py

class SolarPower:
    def __init__(self):
        self.solar_charging = False

    def activate_solar_charging(self):
        self.solar_charging = True
        print("Güneş enerjisi ile şarj etkinleştirildi.")

    def stop_solar_charging(self):
        self.solar_charging = False
        print("Güneş enerjisi ile şarj durduruldu.")
