from app import db
from werkzeug import check_password_hash, generate_password_hash

class User(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	username = db.Column(db.String(128), nullable=False, unique=True)
	password = db.Column(db.String(192), nullable=False)

	def __init__(self, username, password):

		self.username = username
		self.password = generate_password_hash(password)

	def __repr__(self):
		return '<User %r>' % (self.name)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)