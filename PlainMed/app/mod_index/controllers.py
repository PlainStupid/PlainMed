from flask import Blueprint, render_template, abort, request, redirect, url_for
from flask.ext.login import LoginManager, current_user, login_user, logout_user, login_required
from bs4 import BeautifulSoup
import urllib.request
from wtforms import Form, IntegerField, TextField, PasswordField, validators, SelectField
from app import db
from app.mod_index.models import Med

mod_index = Blueprint("index", __name__, url_prefix="/", template_folder="templates")

# Helper function for scraping lyfjaver for medications
def getMeds():
	req = urllib.request.Request('http://lyfjaver.is/lyfjaskra')
	response = urllib.request.urlopen(req)
	bsoup = BeautifulSoup(response)
	tables = bsoup.findAll('td', {'class': 'row1'})

	return [i.string for i in tables]

# Home Page - list of medications
@mod_index.route("/")
@login_required
def index():
    return render_template('meds.html', data=getMeds())

# Page for each medication, for registering meds to your own list
@mod_index.route('Med/<medication>', methods=['GET', 'POST'])
@login_required
def med(medication):

	if medication not in getMeds():
		return render_template('404.html')

	form = RegistrationForm(request.form)

	if request.method == 'POST' and form.validate():
		newMed = Med(str(current_user), medication, form.amount.data, form.intake.data, form.notes.data)
		db.session.add(newMed)
		db.session.commit()
		return render_template('mymeds.html', meds=Med.query.filter_by(user=str(current_user)))

	return render_template('med.html', med=medication, form=form)

# display the meds that the user has registered
@mod_index.route('mymeds')
@login_required
def mymeds():
	return render_template('mymeds.html', meds=Med.query.filter_by(user=str(current_user)))

# The Form that is filled to register new meds
class RegistrationForm(Form):
    amount = IntegerField('Amount', [validators.required(), validators.NumberRange(min=1)])
    intake = SelectField(u'Intake', choices=[('Daily', 'Daily'), ('Every Other Day', 'Every other day'), ('Weekly', 'Weekly'), ('By Need', 'By need')])
    notes = TextField('Notes', [validators.optional()])