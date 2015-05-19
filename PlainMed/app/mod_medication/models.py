from app import db


class Medicine(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    link = db.Column(db.String(), nullable=True)
    chemical = db.Column(db.String(), nullable=True)
    medtype = db.Column(db.String(), nullable=True)


    def __init__(self, name, link, chemical, medtype):
        self.name = name
        self.link = link
        self.chemical = chemical
        self.medtype = medtype


class MedicineUser(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    med = db.Column(db.Integer(), db.ForeignKey('medicine.id', ondelete='CASCADE'))
    amount = db.Column(db.Integer(), nullable=False)
    intake = db.Column(db.String(192), nullable=False)
    amount_type = db.Column(db.String(), nullable=True)
    notes = db.Column(db.String(192), nullable=True)

    def __init__(self, user, med, amount, amount_type, intake, notes):
        self.user = user
        self.med = med
        self.amount = amount
        self.amount_type = amount_type
        self.intake = intake
        self.notes = notes


class MedicineConflict(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    med = db.Column(db.Integer(), db.ForeignKey('medicine.id', ondelete='CASCADE'))
    conflict = db.Column(db.Integer(), db.ForeignKey('medicine.id', ondelete='CASCADE'))

    def __init__(self, med, conflict):
        self.med = med
        self.conflict = conflict