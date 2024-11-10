from abc import ABC, abstractmethod

class Verification(ABC):
    def __init__(self, protocol):
        self.status = False
        self.protocol = protocol

    @property
    @abstractmethod
    def check_status(self) -> bool:
        """Check self verfication status"""
        pass

    @abstractmethod
    def verify(self):
        """Do exact verification"""
        pass

    @abstractmethod
    def update_status(self) -> bool:
        """helper to change verfication status in verify() method"""
        pass

    @abstractmethod
    def protocol_getter(self):
        pass