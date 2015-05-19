from flask.ext.wtf import Form
from wtforms import StringField, SelectField, IntegerField, validators

# The Form that is filled to register new meds
class RegistrationForm(Form):
    amount = IntegerField('Amount', [validators.required(), validators.NumberRange(min=1)])

    amount_type = SelectField('Type', choices=[('mg', 'mg'), ('tsp', 'tsp'),
                                               ('tbsp', 'tbsp'),('other','other')])

    intake = SelectField('Intake', choices=[('Daily', 'Daily'), ('Every Other Day', 'Every other day'),
                                            ('Weekly', 'Weekly'), ('By Need', 'By need')])
    notes = StringField('Notes', [validators.optional()])