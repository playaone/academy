from flask import Flask
from dotenv import load_dotenv

load_dotenv()

from app.config import Config
from app.extentions import db

from app.routes.health import health_bp
from app.routes.home import home_bp
from app.routes.info import info_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    app.register_blueprint(home_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(info_bp)
        
    return app