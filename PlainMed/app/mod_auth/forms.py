from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, validators
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    remember_me = BooleanField('Remember me')


class SignupForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('password_again', message='Passwords must match')])
    password_again = PasswordField('Password again', [validators.DataRequired()])