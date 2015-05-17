from flask import Blueprint, render_template, abort, request
from flask.ext.login import LoginManager, current_user, login_user, logout_user, login_required
from bs4 import BeautifulSoup
import urllib.request

mod_index = Blueprint("index", __name__, url_prefix="/", template_folder="templates")


def getMeds():
	req = urllib.request.Request('http://lyfjaver.is/lyfjaskra')
	response = urllib.request.urlopen(req)
	bsoup = BeautifulSoup(response)
	tables = bsoup.findAll('td', {'class': 'row1'})

	return [i.string for i in tables]

@mod_index.route("/")
@login_required
def index():
    return render_template('meds.html', data=getMeds())

@mod_index.route('Med/<medication>')
@login_required
def med(medication):
	if medication in getMeds():
		return render_template('med.html', med=medication)
	else:
		return render_template('404.html')

@mod_index.route('mymeds')
@login_required
def mymeds():
	return render_template('mymeds.html')