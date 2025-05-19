
from cryptography.fernet import Fernet
import os

def load_key():
    key_file = "secret.key"
    if os.path.exists(key_file):
        with open(key_file, "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
        return key

key = load_key()
cipher = Fernet(key)

def encrypt_password(password: str) -> str:
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(token: str) -> str:
    return cipher.decrypt(token.encode()).decode()
