from app import db

class Med(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	user = db.Column(db.String(), nullable=False)
	med = db.Column(db.String(192), nullable=False)
	amount = db.Column(db.Integer(), nullable=False)
	intake = db.Column(db.String(192), nullable=False)
	notes = db.Column(db.String(192), nullable=True)

	def __init__(self, user, med, amount, intake, notes):
		self.user = user
		self.med = med
		self.amount = amount
		self.intake = intake
		self.notes = notes