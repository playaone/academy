from flask import Flask

import app.models  # noqa: F401
from app.config import Config
from app.error_handlers import register_error_handlers
from app.extensions import db
from app.routes.health import health_bp
from app.routes.home import home_bp
from app.routes.info import info_bp
from app.routes.project import projects_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    app.register_blueprint(home_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(info_bp)
    app.register_blueprint(projects_bp)

    register_error_handlers(app=app)

    return app
