from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

mod_index = Blueprint('index', __name__, url_prefix='/', template_folder='templates')

@mod_index.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)