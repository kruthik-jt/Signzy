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


@app.route('/')
def root():
	return redirect(url_for('index'))

