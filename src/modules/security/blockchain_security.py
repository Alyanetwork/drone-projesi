# blockchain_security.py

import hashlib

class BlockchainSecurity:
    def __init__(self):
        self.chain = []

    def create_block(self, data):
        block = {
            "data": data,
            "hash": self.calculate_hash(data)
        }
        self.chain.append(block)
        print(f"Yeni blok eklendi: {block}")

    def calculate_hash(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

    def verify_chain(self):
        print("Blockchain zinciri doğrulanıyor...")
        for i in range(1, len(self.chain)):
            if self.chain[i]["hash"] != self.calculate_hash(self.chain[i]["data"]):
                print("Blockchain zincirinde hata tespit edildi.")
                return False
        print("Blockchain zinciri güvenli.")
        return True
