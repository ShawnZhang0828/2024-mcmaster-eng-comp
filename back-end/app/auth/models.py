from werkzeug.security import generate_password_hash, check_password_hash
from .EncryptionProtocol.EncryptionManager import EManager

# Mock database
users_db = {}

# Build encryption manager and find current protocol
manager = EManager()
current_protocol = manager.random_use()

class User:
    def __init__(self, username, password_hash, nickname):
        self.username = username
        self.password_hash = password_hash
        self.nickname = nickname
        self.key = manager.get_key(manager.keymap, current_protocol.protocolID)


def create_user(username, password, nickname):
    password_hash = generate_password_hash(password)
    password_hash = encrypt(current_protocol, password_hash)
    users_db[username] = User(username, password_hash, nickname)

def check_user_exist(username):
    return (username in users_db)

def verify_user(username, password):
    user = users_db.get(username)
    password_hash = user.password_hash if user else None
    if password_hash:
            key = user.key
            p = manager.get_protocol(manager.keymap[key])
            password_hash = decrypt(p, password_hash)
            if check_password_hash(password_hash, password):
                return True
    return False

def get_user_nickname(username):
    return users_db.get(username).nickname

def encrypt(protocol, password_hash):
    return protocol.encrypt(password_hash)

def decrypt(protocol, password_hash):
    return protocol.decrypt(password_hash)

