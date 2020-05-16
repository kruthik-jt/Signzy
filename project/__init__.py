from flask import Flask,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///home_auto.db' #sqlalchemy database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='SIGNZY' #Secret key for csrf tokens
modus=Modus(app) #handle method overrides
db=SQLAlchemy(app)

from project.devices.views import devices_blueprint #device blueprint
from project.actions.views import actions_blueprint #action blueprint


@app.route('/')
def root():
	return redirect(url_for('devices.index'))

app.register_blueprint(actions_blueprint,url_prefix='/actions')#registering action blueprint
app.register_blueprint(devices_blueprint,url_prefix='/devices')#registering device blueprint



