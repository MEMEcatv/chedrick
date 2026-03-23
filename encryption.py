import os
import hashlib
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import XOR


# Function to read encryption key from file or generate from password
def read_key(key_file=None, password=None, salt=None):
    if key_file and os.path.exists(key_file):
        return load_key_file(key_file)
    elif password and salt:
        return generate_key(password, salt)
    else:
        raise ValueError("Either a key file or password and salt must be provided.")


# Function to encrypt data using XOR and SHA256
def encrypt_data(data, key):
    # Expand key using SHA256
    expanded_key = hashlib.sha256(key).digest()
    cipher = XOR.new(expanded_key)
    return cipher.encrypt(data)


# Function to decrypt data using XOR
def decrypt_data(encrypted_data, key):
    expanded_key = hashlib.sha256(key).digest()
    cipher = XOR.new(expanded_key)
    return cipher.decrypt(encrypted_data)


# Function to derive key from password using PBKDF2
def generate_key(password, salt, iterations=100000):
    return PBKDF2(password, salt, dkLen=32, count=iterations)


# Function to load raw binary key from file
def load_key_file(filepath):
    with open(filepath, 'rb') as key_file:
        return key_file.read()


# Function to validate key format and length
def validate_key(key):
    if len(key) != 32:
        raise ValueError("Invalid key length. Key must be 32 bytes.")
    # Add further validation as needed

