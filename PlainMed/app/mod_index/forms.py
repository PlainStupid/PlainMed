from flask.ext.wtf import Form
from wtforms import StringField, SelectField, PasswordField, IntegerField, BooleanField, validators

# The Form that is filled to register new meds
class RegistrationForm(Form):
    amount = IntegerField('Amount', [validators.required(), validators.NumberRange(min=1)])
    intake = SelectField(u'Intake', choices=[('Daily', 'Daily'), ('Every Other Day', 'Every other day'), ('Weekly', 'Weekly'), ('By Need', 'By need')])
    notes = StringField('Notes', [validators.optional()])