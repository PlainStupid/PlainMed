from flask import Blueprint, render_template
from flask.ext.login import login_required

mod_index = Blueprint("index", __name__, url_prefix="/", template_folder="templates")


@mod_index.route("/")
@login_required
def index():
    return render_template("index.html")