# -*- coding: utf-8 -*-
# 
from flask import Flask, flash, redirect, url_for, request, get_flashed_messages, render_template, session, g
from flask.ext.login import LoginManager, current_user, login_user, logout_user, login_required
import rlcompleter, pdb
from flask.ext.sqlalchemy import SQLAlchemy
import jinja2

app = Flask(__name__)
app.config.from_object("config")

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
	return render_template("404.html"), 404

from app.mod_auth.models import User

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


# Just redirect to login without giving next=args
@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect(url_for("auth.login"))

template_dir = './templates'
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)
    
# Import a module / component using its blueprint handler variable
from app.mod_index.controllers import mod_index as index_module
from app.mod_auth.controllers import mod_auth as authentication_module

# Register blueprints
app.register_blueprint(index_module)
app.register_blueprint(authentication_module)

db.create_all()