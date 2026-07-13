from flask import render_template, Blueprint
from flask_login import login_required
from services.security import admin_required

#@app.route("/admin")
admin=Blueprint("admin",__name__)
@admin.route("/admin")
@login_required
@admin_required
def admin_panel():

    return render_template("admin.html")