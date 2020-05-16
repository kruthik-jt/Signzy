from flask_wtf import FlaskForm
from wtforms import StringField,validators

#form vaidation for while creating adding devices
class DeviceForm(FlaskForm):
	dev_name=StringField('Device name:',[validators.DataRequired()])
	dev_room=StringField('Device Room:',[validators.DataRequired()])

#used to retain csrf tokens
class DeleteForm(FlaskForm):
	pass