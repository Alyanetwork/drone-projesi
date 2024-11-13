# modules/security/encryption.py

from Crypto.Cipher import AES
import base64
from config import AES_KEY

class Encryption:
    @staticmethod
    def encrypt_message(message):
        cipher = AES.new(AES_KEY, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
        return base64.b64encode(nonce + ciphertext).decode('utf-8')

    @staticmethod
    def decrypt_message(ciphertext):
        data = base64.b64decode(ciphertext)
        nonce = data[:16]
        ciphertext = data[16:]
        cipher = AES.new(AES_KEY, AES.MODE_EAX, nonce=nonce)
        return cipher.decrypt(ciphertext).decode('utf-8')
