from app import db

class User(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	username = db.Column(db.String(128), nullable=False, unique=True)
	password = db.Column(db.String(192), nullable=False)

	def __init__(self, username, password):

		self.username     = username
		self.password = password

	def __repr__(self):
		return '<User %r>' % (self.name)        