from flask_wtf import FlaskForm
from wtforms import StringField,validators


class DeviceForm(FlaskForm):
	dev_name=StringField('Device name:',[validators.DataRequired()])
	dev_room=StringField('Device Room:',[validators.DataRequired()])
class DeleteForm(FlaskForm):
	pass