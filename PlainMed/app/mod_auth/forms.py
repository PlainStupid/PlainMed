from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, validators
from app.mod_auth.models import User
from werkzeug import check_password_hash, generate_password_hash

class LoginForm(Form):
	username = StringField('Username', [validators.Required()])
	password = PasswordField('Password', [validators.Required()])

	def __init__(self, *args, **kwargs):
	        Form.__init__(self, *args, **kwargs)
	        self.user = None


	def validate_on_submit(self):
		rv = Form.validate(self)
		if not rv:
			return False

		user = User.query.filter_by(username=self.username.data).first()

		if user is None:
			self.username.errors.append("Unknown username")
			return False

		if not check_password_hash(user.password, self.password.data):
			self.password.error.append("Invalid password")
			return False

		self.user = user
		return True