# -*- coding: utf-8 -*-
# 
from flask import Flask, redirect, url_for, render_template, g
from flask.ext.login import LoginManager, current_user
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


@app.before_request
def before_request():
    g.user = current_user


# Just redirect to login without giving next=args
@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect(url_for("auth.login"))


template_dir = './templates'
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)

# Import a module / component using its blueprint handler variable
from app.mod_medication.controllers import mod_medication as medicine_module
from app.mod_auth.controllers import mod_auth as authentication_module
from app.mod_index.controllers import mod_index as index_module

# Register blueprints
app.register_blueprint(medicine_module)
app.register_blueprint(authentication_module)
app.register_blueprint(medicine_module)
app.register_blueprint(index_module)

db.create_all()