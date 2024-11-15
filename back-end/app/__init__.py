from flask import Flask
from flask_cors import CORS
from .config import config

def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins": "*", "allow_headers": "*"}})

    app.config.from_object(config)
    
    # Register blueprints
    from .auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
    
    return app
