from flask import redirect,render_template,request,url_for,flash,Blueprint
from project.actions.forms import LogForm,DeleteForm
from project.models import Action,Device
from project import db
import datetime
#Creating actions blueprint
actions_blueprint=Blueprint(
	'actions',
	__name__,
	template_folder='templates'
	)

#lists all the logs for a particular device
@actions_blueprint.route('/<int:dev_id>',methods=['GET','POST'])
def index(dev_id):
	if request.method=='POST':
		time_stamp=str(datetime.datetime.now())
		new_log=Action(request.form['status'],time_stamp,dev_id)
		db.session.add(new_log)
		db.session.commit()
		print(dev_id)
		return redirect(url_for('actions.index',dev_id=dev_id))
	return render_template('actions/index.html',device=Device.query.get(dev_id))
#add new logs or perform actions on a device
@actions_blueprint.route('/new/<int:dev_id>')
def new(dev_id):
	return render_template('actions/new.html',device=Device.query.get(dev_id))
