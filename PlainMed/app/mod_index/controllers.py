from flask import Blueprint, render_template, abort, request, redirect, url_for, g
from flask.ext.login import LoginManager, current_user, login_user, logout_user, login_required
from bs4 import BeautifulSoup
import urllib.request
from wtforms import Form, IntegerField, TextField, PasswordField, validators, SelectField
from app import db
from app.mod_medication.models import MedicineUser, Medicine, MedicineConflict

from app.mod_medication.forms import RegistrationForm

mod_index = Blueprint("index", __name__, url_prefix="/", template_folder="templates")

@mod_index.route("/")
@login_required
def index():
    return render_template("index.html")