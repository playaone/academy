from app import app

@app.route("/")
def home():
    return {
        "message": "welcome to the Engineering Journey Platform API"
    }
    
@app.route("/health")
def health():
    return {
        "status": "ok",
        "service": "backend"
    }