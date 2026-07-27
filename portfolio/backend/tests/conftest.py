import pytest

from app import create_app
from app.config import TestConfig
from app.extensions import db

@pytest.fixture
def app(tmp_path):
    
    database_file = tmp_path / "test.db"
    
    class TemporaryTestConfig(TestConfig):
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{database_file}"
    
    
    app = create_app(TemporaryTestConfig)
    
    with app.app_context():
        db.create_all()
        
        yield app
        
        db.session.remove()
        db.drop_all()
        
@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()