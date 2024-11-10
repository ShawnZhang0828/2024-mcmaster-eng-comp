
from IEnDecryption import Encryption
from self_fernet import Fernet_S
from self_rsa import RSA_S
import random

class EManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialize some attributes only once
        if not hasattr(self, 'initialized'):  # To ensure it's only initialized once
            self.count = 0
            self.protocols = dict()
            self.initialized = True
            self.all_ids = {f"{i:03d}" for i in range(1000)}  # Set of all possible IDs
            for _ in range(10):
                self.random_build()


    def build_fernet(self):
        if len(self.protocols) == 999:
            print("Amount of protocols has reached the maximum")
            return None

        if self.all_ids == {}:
            print("No more unique protocol IDs available")
            return None

        random_id = random.choice(list(self.all_ids))  # Pick a random unused ID
        self.all_ids.remove(random_id)

        self.protocols[random_id] = Fernet_S(random_id)
        return random_id
    
    def build_RSA(self):
        if len(self.protocols) == 999:
            print("Amount of protocols has reached the maximum")
            return None

        if self.all_ids == {}:
            print("No more unique protocol IDs available")
            return None

        random_id = random.choice(list(self.all_ids))  # Pick a random unused ID
        self.all_ids.remove(random_id)

        self.protocols[random_id] = RSA_S(random_id)
        return random_id
    
    def random_build(self):
        # Define possible protocols you can build
        protocol_types = ['FERNET', 'RSA']

        # Randomly choose a protocol type
        chosen_protocol_type = random.choice(protocol_types)
        
        # Build the chosen protocol
        if chosen_protocol_type == 'FERNET':
            return self.build_fernet()  # Call the build method for Fernet protocol
        elif chosen_protocol_type == 'RSA':
            return self.build_RSA()  # Call the build method for RSA protocol
        else:
            print("No valid protocol type found.")
        return None
    
    def random_use(self):
        # Check if there are any protocols in the dictionary
        if not self.protocols:
            print("No protocols available")
            return None
        
        # Randomly select a protocol ID
        random_protocol_id = random.choice(list(self.protocols.keys()))
        
        # Return the selected protocol
        return self.protocols[random_protocol_id]
        
    
    def del_protocol(self, protocolID):
        if protocolID in self.protocols:
            del self.protocols[protocolID]
            print(f"Protocol {protocolID} deleted.")
        else:
            print(f"Protocol {protocolID} not found.")
    
    def del_all(self):
        # Clear all protocols
        self.protocols.clear()
        print("All protocols deleted.")

    def get_protocol(self, protocolID):
        if protocolID in self.protocols:
            return self.protocols[protocolID]
        else:
            print(f"Protocol {protocolID} not found.")
            return None
        