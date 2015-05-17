# -*- coding: utf-8 -*-
# 
from flask import Flask, flash, redirect, url_for, request, get_flashed_messages, render_template, session, g
from flask.ext.login import LoginManager, current_user, login_user, logout_user, login_required
import rlcompleter, pdb
from flask.ext.sqlalchemy import SQLAlchemy

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
    
# Import a module / component using its blueprint handler variable
from app.mod_index.controllers import mod_index as index_module
from app.mod_auth.controllers import mod_auth as authentication_module

# Register blueprints
app.register_blueprint(index_module)
app.register_blueprint(authentication_module)

db.create_all()