from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, validators
from app.mod_auth.models import User
from werkzeug import check_password_hash, generate_password_hash


class LoginForm(Form):
	username = StringField('Username', [validators.Required()])
	password = PasswordField('Password', [validators.Required()])