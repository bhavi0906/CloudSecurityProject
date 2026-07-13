from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import login_user, logout_user
from extensions import bcrypt, login_manager
from models import User
from forms import RegistrationForm, LoginForm
from extensions import db

auth= Blueprint("auth",__name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth.route("/")
def home():
    return redirect(url_for("auth.login"))


@auth.route("/register", methods=["GET", "POST"])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
            role="User"
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration Successful!", "success")

        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(
                user.password,
                form.password.data):

            login_user(user)

            return redirect(url_for("dashboard.dashboard_page"))

        flash("Invalid Email or Password", "danger")

    return render_template("login.html", form=form)


@auth.route("/logout")
def logout():

    logout_user()

    return redirect(url_for("auth.login"))