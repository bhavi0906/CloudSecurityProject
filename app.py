from flask import Flask
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def home():
    return "<h1>Cloud Security Dashboard</h1><p>Backend configured successfully!</p>"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()   # Creates users.db tables if they don't exist
    app.run(host="127.0.0.1", port=5000, debug=True)