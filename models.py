from extensions import db
from flask_login import UserMixin



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20),nullable=False, default="User")

class UploadedFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(db.String(255), nullable=False)

    filepath = db.Column(db.String(500), nullable=False)

    uploaded_by = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    upload_time = db.Column(
        db.DateTime,
        default=db.func.current_timestamp()
    )    