from flask_wtf import FlaskForm
from wtforms import StringField,validators


class LogForm(FlaskForm):
	dev_status=StringField('Status:',[validators.DataRequired()])

class DeleteForm(FlaskForm):
	pass