"""pip install pycryptodome"""
"""RSA method, Asymmetric"""
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from IEnDecryption import Encryption

class RSA_S(Encryption):
    PROCOTOL_TYPE = "RSA"

    def __init__(self, protocolID):
        self.key = RSA.generate(2048)
        self.public_key = self.key.publickey()
        super().__init__(protocolID)
        self.protocol_name = self.PROCOTOL_TYPE + self.protocolID

    
    def encrypt(self, data):
        """Do exact encrypt"""
        if type(data) == str:
            msg_bytes = data.encode()
        else:
            msg_bytes = data
        cipher_rsa = PKCS1_OAEP.new(self.public_key)
        encrypted_message = cipher_rsa.encrypt(msg_bytes)
        return encrypted_message
    

    def decrypt(self, data):
        """Do exact decrypt"""
        cipher_rsa = PKCS1_OAEP.new(self.key)
        decrypted_message = cipher_rsa.decrypt(data).decode()
        return decrypted_message


    def protocol_getter(self):
        """Show exact protocol is used"""
        return [self.PROCOTOL_TYPE, self.protocol_name]