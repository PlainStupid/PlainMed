# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort, redirect, url_for, request, flash, session, g
from app.mod_auth.forms import LoginForm, SignupForm
from app.mod_auth.models import User
from flask.ext.login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug import check_password_hash, generate_password_hash
from app import db

mod_auth = Blueprint("auth", __name__, url_prefix="/auth", template_folder="templates")

@mod_auth.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()

	if request.method == 'POST':
		if request.form["username"] is "":
			flash("Username is needed")

		elif request.form["password"] is "":
			flash("Password is needed")
		else:
			rememberme = True if "remember_me" in request.form else False
			user = User.query.filter_by(username=request.form['username']).first()
			if user and check_password_hash(user.password, request.form["password"]):
				login_user(user, remember=rememberme)
				return redirect(url_for("index.index"))
			else:
				flash("Wrong username/password")

	return render_template("login.html", form=form)

@mod_auth.route("/signup", methods=["GET", "POST"])
def signup():
	form = SignupForm()

	if request.method == "POST":
		newUsername = request.form["username"]
		newPassword = request.form["password"]
		newPassword2 = request.form["password_again"]

		if newUsername is "":
			flash("Username is needed")
		elif newPassword is "" or newPassword2 is "":
			flash("Both password fields are needed")
		else:
			checkUser = User.query.filter_by(username=newUsername).first()
			if checkUser:
				flash("This username exists!")
			else:
				if newPassword==newPassword2:
					newUser = User(newUsername, newPassword)
					db.session.add(newUser)
					db.session.commit()

					return redirect(url_for("auth.login"))
				else:
					flash("The password doesn't match")

	return render_template("signup.html", form=form)

@mod_auth.route('/logout/')
@login_required
def logout():
	logout_user()
	return redirect(url_for("auth.login"))