import os
from dotenv import load_dotenv
#from azure.monitor.opentelemetry import configure_azure_monitor

load_dotenv()

if os.getenv("WEBSITE_SITE_NAME"):
    from azure.monitor.opentelemetry import configure_azure_monitor

    if connection_string:
        configure_azure_monitor(connection_string=connection_string)
#connection_string=os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")

#if connection_string:
#    configure_azure_monitor(connection_string=connection_string)

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