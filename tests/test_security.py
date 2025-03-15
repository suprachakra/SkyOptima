"""
test_security.py: Unit tests for data privacy (encryption/decryption) functions.
"""

import unittest
from src.security.data_privacy import generate_key, encrypt_data, decrypt_data

class TestSecurity(unittest.TestCase):

    def test_encryption_decryption(self):
        key = generate_key()
        original_text = "Sensitive SkyOptima Data"
        encrypted = encrypt_data(key, original_text)
        decrypted = decrypt_data(key, encrypted)
        self.assertEqual(original_text, decrypted)

if __name__ == '__main__':
    unittest.main()
