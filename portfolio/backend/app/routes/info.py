from flask import Blueprint, current_app

info_bp = Blueprint("info", __name__)


@info_bp.get("/info")
def info():
    return {
        "environment": current_app.config.get("DEBUG"),
        "database_host": current_app.config.get("DB_HOST"),
    }