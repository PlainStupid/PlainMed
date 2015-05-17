# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort, redirect, url_for, request, flash, session, g
from jinja2 import TemplateNotFound
from app.mod_auth.forms import LoginForm
from app.mod_auth.models import User
from flask.ext.login import LoginManager, current_user, login_user, logout_user, login_required

from werkzeug import check_password_hash, generate_password_hash


mod_auth = Blueprint("auth", __name__, url_prefix="/auth", template_folder="templates")

@mod_auth.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()

	if request.method == 'POST':
		user = User.query.filter_by(username=request.form['username']).first()
		if user and check_password_hash(user.password, request.form["password"]):
			login_user(user)
			return redirect(url_for("index.index"))
		else:
			flash("Wrong username/password")

	return render_template("login.html", form=form)

@mod_auth.route("/signup", methods=["GET", "POST"])
def signup():
	newUser = User("ragnar", "ragnar")
	db.session.add(newUser)
	db.session.commit()

	return redirect(url_for("auth.login"))

@mod_auth.route('/logout/')
def logout():
	logout_user()
	return redirect(url_for("auth.login"))