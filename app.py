from flask import Flask
from config import Config
from extensions import db, bcrypt, login_manager


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

from routes.auth import auth
app.register_blueprint(auth)
from routes.dashboard import dashboard
app.register_blueprint(dashboard)
from routes.storage import storage
app.register_blueprint(storage)
from routes.admin import admin
app.register_blueprint(admin)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)