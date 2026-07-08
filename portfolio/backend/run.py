from app import create_app
from app.extensions import db

app = create_app()

with app.app_context():
    print("Database URI:")
    print(app.config["SQLALCHEMY_DATABASE_URI"])

if __name__ == "__main__":
    app.run(debug=True)