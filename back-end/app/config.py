import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "1234567")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "abcdefg")

config = Config()
