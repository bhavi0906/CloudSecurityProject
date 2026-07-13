from flask import render_template,  Blueprint 
from flask_login import login_required, current_user



#@app.route("/dashboard")
dashboard=Blueprint("dashboard",__name__)
@dashboard.route("/dashboard")
@login_required
def dashboard_page():
    return render_template("dashboard.html",user=current_user)