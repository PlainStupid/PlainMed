from app import db
from werkzeug import check_password_hash, generate_password_hash
from flask.ext.login import UserMixin

class Medicine(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name