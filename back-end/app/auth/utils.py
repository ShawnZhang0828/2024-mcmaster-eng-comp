import jwt
from datetime import datetime, timedelta
from app.config import config
from auth.EncryptionProtocol.EncryptionManager import EManager

def generate_token(username):
    payload = {
        "username": username,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, config.JWT_SECRET_KEY, algorithm="HS256")

def verify_token(token):
    try:
        payload = jwt.decode(token, config.JWT_SECRET_KEY, algorithms=["HS256"])
        return payload["username"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    
def encrypt(protocol, password_hash):
    return protocol.encrypt(password_hash)

def decrypt(protocol, password_hash):
    return protocol.decrypt(password_hash)

