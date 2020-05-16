from flask_wtf import FlaskForm
from wtforms import StringField,validators

#Form validation when new actions are performed on a device
class LogForm(FlaskForm):
	dev_status=StringField('Status:',[validators.DataRequired()])

#Used to retain csrf tokens
class DeleteForm(FlaskForm):
	pass