from flask import Flask
from config import Config
from extensions import db, bcrypt, login_manager
from routes.storage import *

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

from routes.auth import *
from routes.dashboard import *
from routes.admin import *

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)