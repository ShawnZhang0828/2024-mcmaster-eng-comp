"""This interface will be used to add encryption protocol to en/decryption for data manipulation"""

from abc import ABC, abstractmethod

class Encryption(ABC):
    def __init__(self, protocolID):
        self.protocolID = protocolID

    @abstractmethod
    def encrypt(self):
        """Do exact encrypt"""
        pass


    @abstractmethod
    def decrypt(self):
        """Do exact decrypt"""
        pass


    @abstractmethod
    def protocol_getter(self):
        """Show exact protocol is used"""
        pass