"""These Interface will be used for add extra verification methods;
Username&password verfication is implemented in routes.py"""
from abc import ABC, abstractmethod

class Verification(ABC):
    def __init__(self, protocolID):
        self.status = False
        self.protocolID = protocolID

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
        """Helper to change verfication status in verify() method"""
        pass

    @abstractmethod
    def protocol_getter(self):
        """Show exact protocol is used"""
        pass