from flask import redirect,render_template,request,url_for,flash,Blueprint
from project.actions.forms import LogForm,DeleteForm
from project.models import Action
from project import db


actions_blueprint=Blueprint(
	'actions',
	__name__,
	template_folder='templates'
	)


@actions_blueprint.route('/actions/<int:dev_id>',methods=['GET','POST'])
def action_index(dev_id):
	if request.method=='POST':
		time_stamp=str(datetime.datetime.now())
		new_log=Action(request.form['status'],time_stamp,dev_id)
		db.session.add(new_log)
		db.session.commit()
		print(dev_id)
		return redirect(url_for('action_index',dev_id=dev_id))
	return render_template('actions/index.html',device=Device.query.get(dev_id))

@actions_blueprint.route('/actions/new/<int:dev_id>')
def action_new(dev_id):
	return render_template('actions/new.html',device=Device.query.get(dev_id))
