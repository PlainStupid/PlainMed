from flask import Blueprint, render_template, abort, request, redirect, url_for, g
from flask.ext.login import LoginManager, current_user, login_user, logout_user, login_required
from bs4 import BeautifulSoup
import urllib.request
from wtforms import Form, IntegerField, TextField, PasswordField, validators, SelectField
from app import db
from app.mod_index.models import MedicineUser, Medicine

from app.mod_index.forms import RegistrationForm

mod_index = Blueprint("index", __name__, url_prefix="/", template_folder="templates")

# Home Page - list of medications
@mod_index.route("/")
@login_required
def index():
    medications = Medicine.query.all()

    return render_template('meds.html', data=medications)


# Page for each medication, for registering meds to your own list
@mod_index.route('Med/<medication>', methods=['GET', 'POST'])
@login_required
def med(medication):
    gotMed = Medicine.query.filter_by(shortname=medication).first()

    if gotMed is None:
        return abort(404)

    form = RegistrationForm(request.form)

    if request.method == 'POST':
        print("Valid Med")
        newMed = MedicineUser(g.user.id, medication, form.amount.data, form.intake.data, form.notes.data)
        db.session.add(newMed)
        db.session.commit()
        return redirect(url_for("index.mymeds"))

    return render_template('med.html', med=gotMed, form=form)


# display the meds that the user has registered
@mod_index.route('mymeds')
@login_required
def mymeds():
    medications=MedicineUser.query.filter_by(user=g.user.id)

    return render_template('mymeds.html', meds=medications)