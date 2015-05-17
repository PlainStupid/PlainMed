from app import db
from app.mod_auth.models import User


class Medicine(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    shortname = db.Column(db.String(), nullable=False, unique=True)

    def __init__(self, name, shortname):
        self.name = name
        self.shortname = shortname


class MedicineUser(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    med = db.Column(db.Integer(), db.ForeignKey('medicine.id', ondelete='CASCADE'))
    amount = db.Column(db.Integer(), nullable=False)
    intake = db.Column(db.String(192), nullable=False)
    notes = db.Column(db.String(192), nullable=True)

    def __init__(self, user, med, amount, intake, notes):
        self.user = user
        self.med = med
        self.amount = amount
        self.intake = intake
        self.notes = notes

class MedicineConflict(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    med = db.Column(db.Integer(), db.ForeignKey('medicine.id', ondelete='CASCADE'))
    conflict = db.Column(db.Integer(), db.ForeignKey('medicine.id', ondelete='CASCADE'))

    def __init__(self, med, conflict):
        self.med = med
        self.conflict = conflict