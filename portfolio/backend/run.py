from app import create_app

app = create_app()

with app.app_context():
    print("Database URI:")
    print(app.config["SQLALCHEMY_DATABASE_URI"])

if __name__ == "__main__":
    app.run(debug=True)
