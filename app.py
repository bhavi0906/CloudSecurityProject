from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Secret key used for sessions and forms
app.config["SECRET_KEY"] = "cloudsecurityproject"

# Create database folder if it doesn't exist
os.makedirs("database", exist_ok=True)

# SQLite database path
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/users.db"

# Disable modification tracking
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
db = SQLAlchemy(app)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True, nullable=False)

    email = db.Column(db.String(150), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)


@app.route("/")
def home():
    return "<h1>Cloud Security Dashboard</h1>"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
