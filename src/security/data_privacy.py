"""
data_privacy.py: Implements functions for data encryption and decryption to ensure data privacy.
Uses the cryptography library.
"""

from cryptography.fernet import Fernet
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DataPrivacy")

def generate_key() -> bytes:
    """Generate a new encryption key."""
    key = Fernet.generate_key()
    logger.info("Encryption key generated.")
    return key

def encrypt_data(key: bytes, data: str) -> bytes:
    """Encrypt data using the provided key.
    
    Args:
        key (bytes): Encryption key.
        data (str): Data to encrypt.
    
    Returns:
        bytes: Encrypted data.
    """
    f = Fernet(key)
    encrypted = f.encrypt(data.encode())
    logger.info("Data encrypted.")
    return encrypted

def decrypt_data(key: bytes, token: bytes) -> str:
    """Decrypt data using the provided key.
    
    Args:
        key (bytes): Encryption key.
        token (bytes): Encrypted data.
    
    Returns:
        str: Decrypted data.
    """
    f = Fernet(key)
    decrypted = f.decrypt(token).decode()
    logger.info("Data decrypted.")
    return decrypted

if __name__ == "__main__":
    key = generate_key()
    original_data = "Sensitive SkyOptima data"
    encrypted_data = encrypt_data(key, original_data)
    print("Encrypted:", encrypted_data)
    decrypted_data = decrypt_data(key, encrypted_data)
    print("Decrypted:", decrypted_data)
