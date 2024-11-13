# route_planning.py

from config import WAYPOINTS

class RoutePlanning:
    def __init__(self):
        self.route = WAYPOINTS

    def get_dynamic_route(self):
        print("Dinamik Rota Oluşturuluyor...")
        return self.route

    def update_route(self, avoid_obstacle=False):
        if avoid_obstacle:
            print("Engellerden Kaçınmak İçin Yeni Rota Belirleniyor...")
            self.route = self.generate_alternative_route()
    
    def generate_alternative_route(self):
        print("Alternatif Rota Hesaplanıyor...")
        return [{"latitude": 40.714276, "longitude": -74.006000, "altitude": 20}]
