"""Need to run 
`pip install cryptography`
in terminal."""
"""FERNET method, Symmetric"""

from cryptography.fernet import Fernet
from IEnDecryption import Encryption

class Fernet_S(Encryption):
    PROCOTOL_TYPE = "FERNET"

    def __init__(self, protocolID):
        self.key = Fernet.generate_key()
        self.fernet_cipher = Fernet(self.key)
        super().__init__(protocolID)
        self.protocol_name = self.PROCOTOL_TYPE + self.protocolID

    
    def encrypt(self, data):
        """Do exact encrypt"""
        if type(data) == str:
            msg_bytes = data.encode()
        else:
            msg_bytes = data
        encrypted_message = self.fernet_cipher.encrypt(msg_bytes)
        return encrypted_message
    

    def decrypt(self, data):
        """Do exact decrypt"""
        decrypted_message = self.fernet_cipher.decrypt(data).decode()
        return decrypted_message


    def protocol_getter(self):
        """Show exact protocol is used"""
        return [self.PROCOTOL_TYPE, self.protocol_name]