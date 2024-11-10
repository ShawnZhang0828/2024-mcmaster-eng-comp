from werkzeug.security import generate_password_hash, check_password_hash

# Mock database
users_db = {}

class User:
    def __init__(self, username, password_hash, nickname):
        self.username = username
        self.password_hash = password_hash
        self.nickname = nickname


def create_user(username, password, nickname):
    password_hash = generate_password_hash(password)
    users_db[username] = User(username, password_hash, nickname)

def check_user_exist(username):
    return (username in users_db)

def verify_user(username, password):
    user = users_db.get(username)
    password_hash = user.password_hash if user else None
    if password_hash and check_password_hash(password_hash, password):
        return True
    return False

def get_user_nickname(username):
    return users_db.get(username).nickname