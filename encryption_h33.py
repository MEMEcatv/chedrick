from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import os

class H33Encryption:
    def __init__(self, password: str, salt: bytes = None):
        self.salt = salt or os.urandom(16)
        self.key = self.generate_key(password)

    def generate_key(self, password: str) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    def encrypt(self, data: str) -> bytes:
        fernet = Fernet(self.key)
        return fernet.encrypt(data.encode())

    def decrypt(self, token: bytes) -> str:
        fernet = Fernet(self.key)
        return fernet.decrypt(token).decode()