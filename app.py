from flask import Flask,request,redirect,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from forms import DeviceForm,LogForm,DeleteForm
import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///home_auto.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='SIGNZY'
modus=Modus(app)
db=SQLAlchemy(app)

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
@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/devices',methods=['GET','POST'])
def index():
	delete_form=DeleteForm()
	if request.method=='POST':
		device_form=DeviceForm(request.form)
		if(device_form.validate()):
			new_dev=Device(request.form['dev_name'],request.form['dev_room'])
			db.session.add(new_dev)
			db.session.commit()
			return redirect(url_for('index'))
		else:
			return render_template('devices/new.html',form=device_form)
	return render_template('devices/index.html',devices=Device.query.all(),delete_form=delete_form)
@app.route('/devices/new')
def new():
	device_form=DeviceForm()
	return render_template('devices/new.html',form=device_form)

@app.route('/devices/<int:id>',methods=['POST','GET'])
def edit(id):
	delete_form=DeleteForm(request.form)
	print(request.form)
	if(delete_form.validate()):
		del_device=Device.query.get(id)
		db.session.delete(del_device)
		db.session.commit()
	return render_template('devices/index.html',devices=Device.query.all(),delete_form=delete_form)

@app.route('/actions/<int:dev_id>',methods=['GET','POST'])
def action_index(dev_id):
	if request.method=='POST':
		time_stamp=str(datetime.datetime.now())
		new_log=Action(request.form['status'],time_stamp,dev_id)
		db.session.add(new_log)
		db.session.commit()
		print(dev_id)
		return redirect(url_for('action_index',dev_id=dev_id))
	return render_template('actions/index.html',device=Device.query.get(dev_id))

@app.route('/actions/new/<int:dev_id>')
def action_new(dev_id):
	return render_template('actions/new.html',device=Device.query.get(dev_id))


if __name__=='__main__':
	app.run(debug=True,port=5000)