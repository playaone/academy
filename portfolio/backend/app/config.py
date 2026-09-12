import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INSTANCE_DIR = BASE_DIR / "instance"
DATABASE_PATH = INSTANCE_DIR / "project.sql"

INSTANCE_DIR.mkdir(parents=True, exist_ok=True)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "development-secret")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    # SQLALCHEMY_DATABASE_URI = (
    #     f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    #     f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    # )

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_PATH.as_posix()}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    TESTING = True

    SECRET_KEY = "testing-secret"

    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
