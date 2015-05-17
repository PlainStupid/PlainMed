from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, validators
from wtforms.validators import DataRequired, ValidationError
from app.mod_auth.models import User
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from werkzeug import check_password_hash


class LoginForm(Form):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    remember_me = BooleanField('Remember me')

    def validate_password(form, field):
        try:
            user = User.query.filter(User.username == form.username.data).one()
        except (MultipleResultsFound, NoResultFound):
            raise ValidationError("Invalid user")
        if user is None:
            raise ValidationError("Invalid user")
        if not check_password_hash(user.password, form.password.data):
            raise ValidationError("Invalid password")


class SignupForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(),
                                          validators.EqualTo('password_again', message='Passwords must match')])
    password_again = PasswordField('Password again', [validators.DataRequired()])