from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, validators

class LoginForm(Form):
	username = StringField('Username', [validators.Required()])
	password = PasswordField('Password', [validators.Required()])