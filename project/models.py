from project import db


class Device(db.Model):
	__tablename__='Device'
	id=db.Column(db.Integer, primary_key=True)
	dev_name=db.Column(db.Text)
	dev_room=db.Column(db.Text)
	Action=db.relationship("Action", backref='device',lazy='dynamic',cascade='all,delete')

	def __init__(self,dev_name,dev_room):
		self.dev_name=dev_name
		self.dev_room=dev_room

class Action(db.Model):
	__tablename__='Action'
	id=db.Column(db.Integer,primary_key=True)
	dev_status=db.Column(db.Text)
	time_stamp=db.Column(db.Text)
	dev_id=db.Column(db.Integer,db.ForeignKey('Device.id'))
	#Device=relationship("Device",back_populates='Action')

	def __init__(self,dev_status,time_stamp,dev_id):
		self.dev_status=dev_status
		self.time_stamp=time_stamp
		self.dev_id=dev_id