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
