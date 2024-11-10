from werkzeug.security import generate_password_hash, check_password_hash

# Mock database
users_db = {}

def create_user(username, password):
    password_hash = generate_password_hash(password)
    users_db[username] = password_hash

def verify_user(username, password):
    password_hash = users_db.get(username)
    if password_hash and check_password_hash(password_hash, password):
        return True
    return False