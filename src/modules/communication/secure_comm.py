# src/modules/communication/secure_comm.py

from Crypto.Cipher import AES
import base64

class SecureComm:
    def __init__(self, key):
        self.key = key

    def encrypt_message(self, message):
        cipher = AES.new(self.key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
        return base64.b64encode(nonce + ciphertext).decode('utf-8')

    def send_secure_message(self, message):
        encrypted_msg = self.encrypt_message(message)
        print(f"Gönderilen Kriptolu Mesaj: {encrypted_msg}")
        # En yakın kontrol merkezi ile iletişime geçme kodları burada yer alacak
        # (HTTP request, socket bağlantısı vb.)
