from flask import Flask,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///home_auto.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='SIGNZY'
modus=Modus(app)
db=SQLAlchemy(app)

from project.devices.views import devices_blueprint
from project.actions.views import actions_blueprint


@app.route('/')
def root():
	return redirect(url_for('devices.index'))

app.register_blueprint(actions_blueprint,url_prefix='/actions')
app.register_blueprint(devices_blueprint,url_prefix='/devices')



