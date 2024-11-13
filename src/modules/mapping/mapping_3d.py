# mapping_3d.py

import random

class Mapping3D:
    def __init__(self):
        self.map_data = []

    def capture_environment(self):
        print("3D çevre taraması yapılıyor...")
        self.map_data = [{"x": random.uniform(0, 10), "y": random.uniform(0, 10), "z": random.uniform(0, 5)} for _ in range(100)]
        print("3D tarama tamamlandı.")

    def get_map_data(self):
        return self.map_data
