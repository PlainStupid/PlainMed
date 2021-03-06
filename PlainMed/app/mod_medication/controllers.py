from flask import Blueprint, render_template, abort, redirect, url_for, g, flash
from flask.ext.login import login_required
from app import db
from app.mod_medication.models import MedicineUser, Medicine, MedicineConflict

from app.mod_medication.forms import RegistrationForm

mod_medication = Blueprint("medication", __name__, url_prefix="/medicine", template_folder="templates")

# Home Page - list of medications
@mod_medication.route("/")
@login_required
def index():
    medications = Medicine.query.order_by(Medicine.name).all()

    return render_template('medications.html', data=medications)


# Page for each medication, for registering meds to your own list
@mod_medication.route('/add/<medication>', methods=['GET', 'POST'])
@login_required
def addmeds(medication):
    gotMed = Medicine.query.filter_by(link=medication).first()

    if gotMed is None:
        return abort(404)

    form = RegistrationForm()

    if form.validate_on_submit():
        #hasbefore = MedicineUser.query.filter(MedicineUser.med==gotMed.id).first()
        
        getAllFromUser = MedicineUser.query.filter_by(user=g.user.id).all()
        hasbefore = True if gotMed.id in [x.med for x in getAllFromUser] else False

        if hasbefore:
            flash("You have already added this before")
        else:

            newMed = MedicineUser(g.user.id, 
                                    gotMed.id, 
                                    form.amount.data, 
                                    form.amount_type.data, 
                                    form.intake.data,
                                    form.notes.data)
            
            db.session.add(newMed)
            db.session.commit()
            return redirect(url_for(".mymeds"))

    return render_template('addmedication.html', med=gotMed, form=form)


# display the meds that the user has registered
@mod_medication.route('/mymeds')
@login_required
def mymeds():
    medications = db.session.query(MedicineUser, Medicine).join(Medicine)

    return render_template('mymedications.html', meds=medications)


@mod_medication.route('/deleteUsers/<int:id>')
@login_required
def deleteUsers(id):
    mymedication = MedicineUser.query.filter_by(med=id).first()
    db.session.delete(mymedication)
    db.session.commit()
    return redirect(url_for("medication.mymeds"))