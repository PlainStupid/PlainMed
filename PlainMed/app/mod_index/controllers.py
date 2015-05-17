from flask import Blueprint, render_template, abort
from flask.ext.login import LoginManager, current_user, login_user, logout_user, login_required

mod_index = Blueprint("index", __name__, url_prefix="/", template_folder="templates")

@mod_index.route("/")
@login_required
def index():
	return render_template("index.html")