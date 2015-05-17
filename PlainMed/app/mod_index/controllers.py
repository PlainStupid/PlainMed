from flask import Blueprint, render_template, abort

mod_index = Blueprint("index", __name__, url_prefix="/", template_folder="templates")

@mod_index.route("/")
def index():
	return render_template("index.html")