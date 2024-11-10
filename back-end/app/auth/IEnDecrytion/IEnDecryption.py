from abc import ABC, abstractmethod

class Encryption(ABC):
    def __init__(self, protocol):
        self.status = False
        self.protocol = protocol

    @property
    @abstractmethod
    def check_encryption_status(self) -> bool:
        """Check self encryption and decryption status"""
        pass

    @abstractmethod
    def encrypt(self):
        """Do exact encrypt"""
        pass

    @abstractmethod
    def decrypt(self):
        """Do exact decrypt"""
        pass

    @abstractmethod
    def update_status(self) -> bool:
        """helper to change verfication status in verify() method"""
        pass

    @abstractmethod
    def protocol_getter(self):
        pass