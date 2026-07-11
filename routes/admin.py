from flask import render_template
from flask_login import login_required
from app import app
from services.security import admin_required

@app.route("/admin")
@login_required
@admin_required
def admin():

    return render_template("admin.html")