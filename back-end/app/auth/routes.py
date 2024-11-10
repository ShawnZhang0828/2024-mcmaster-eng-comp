from flask import Blueprint, request, jsonify
from .models import create_user, verify_user, check_user_exist, get_user_nickname
from .utils import generate_token, verify_token

auth_bp = Blueprint("auth", __name__)

# Registration endpoint
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    nickname = data.get("nickname")
    if check_user_exist(username):
        return jsonify({"message": "User already exists"}), 400
    create_user(username, password, nickname)
    return jsonify({"message": "User registered successfully"}), 201

# Login endpoint
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if verify_user(username, password):
        token = generate_token(username)
        nickname = get_user_nickname(username)
        return jsonify({"token": token, "nickname": nickname}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# Protected route (example)
@auth_bp.route("/protected", methods=["GET"])
def protected():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message": "Token is missing"}), 401
    username = verify_token(token)
    if not username:
        return jsonify({"message": "Token is invalid or expired"}), 401
    return jsonify({"message": f"Hello, {username}!"}), 200
