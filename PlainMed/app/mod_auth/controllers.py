from flask import Blueprint, render_template, abort, redirect, url_for, request, flash, session
from jinja2 import TemplateNotFound
from app.mod_auth.forms import LoginForm
from werkzeug import check_password_hash, generate_password_hash
from app.mod_auth.models import User
from app import db


mod_auth = Blueprint("auth", __name__, url_prefix="/auth", template_folder="templates")

@mod_auth.route("/")
def index():
    try:
        return redirect(url_for(".login"))
    except TemplateNotFound:
        abort(404)

@mod_auth.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm(request.form)

	if form.validate_on_submit():
		flash("Successfully login as %s" % form.user.username)
		session["user_id"] = form.user.id
		return redirect(url_for("index.index"))
	else:
		print("no validate")
	return render_template("login.html", form=form)


@mod_auth.route("/signup", methods=["GET", "POST"])
def signup():
	newUser = User("ragnar", "ragnar")
	db.session.add(newUser)
	db.session.commit()

	return redirect(url_for("auth.login"))