from flask import Blueprint, render_template, abort, request
from flask.ext.login import LoginManager, current_user, login_user, logout_user, login_required
from bs4 import BeautifulSoup
import urllib.request
from app.mod_med.models import Medicine

mod_med = Blueprint("medicine", __name__, url_prefix="/medicine", template_folder="templates")

@mod_med.route("/info/<med>")
@login_required
def medicine_info(med):
    pass