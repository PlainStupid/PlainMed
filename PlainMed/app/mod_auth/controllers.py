# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for, request
from app.mod_auth.forms import LoginForm, SignupForm
from app.mod_auth.models import User
from flask.ext.login import login_user, logout_user, login_required
from werkzeug import check_password_hash
from app import db

mod_auth = Blueprint("auth", __name__, url_prefix="/auth", template_folder="templates")


@mod_auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        rememberme = True if "remember_me" in request.form else False
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user, remember=rememberme)
            return redirect(url_for("index.index"))

    return render_template("login.html", form=form)


@mod_auth.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        newUsername = request.form["username"]
        newPassword = request.form["password"]
        newPassword2 = request.form["password_again"]

        checkUser = User.query.filter_by(username=newUsername).first()
        if checkUser is None:
            if newPassword == newPassword2:
                newUser = User(newUsername, newPassword)
                db.session.add(newUser)
                db.session.commit()

                return redirect(url_for("auth.login"))

    return render_template("signup.html", form=form)


@mod_auth.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))