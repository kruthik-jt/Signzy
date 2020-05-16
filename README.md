# Signzy
Home automation

## Overview
&nbsp;An extensible and moduarized Home automation system built using Flask and Sql Alchemy.<br>
&nbsp;<b>Flask:</b> Flask is a microframework, makes deploying web applications simpler and faster than other conventional methods.<br>
&nbsp;<b>SqlAlchemy:</b> SqlAlchemy is the python SQL toolkit and ObjectRelationalMapper. It provides an easier interface to communicate with databases with its Classes and objects paradigm.<br><br>
&nbsp;The application allows a user to do the following:<br>
&nbsp;&nbsp;1. Add a new device to the system.<br>
&nbsp;&nbsp;2. Delete an installed device from the system.<br>
&nbsp;&nbsp;3. List all the devices in the system.<br>
&nbsp;&nbsp;4. Perform actions on the system (switching on and switching off a device).<br>
&nbsp;&nbsp;5. Logs of the actions performed on the devices.
## Structuring
Small flask applications can be implemented in a simple way, but larger applications tend to get out of hand and requires to be structured. Structuring a flask applications makes it <b>Highly extensible</b> and <b>modularized</b>. 
<br><br>
&nbsp;<b>M</b>odel <b>V</b>iew <b>C</b>ontroller design pattern is implemented.<br>
&nbsp;&nbsp;<b>Model:</b> A model is responsible for managing data storage.<br>
&nbsp;&nbsp;<b>View:</b> A view is what is presented to the user.<br>
&nbsp;&nbsp;<b>Controller:</b> The brain behind the operations.<br>

## Installations
&nbsp;- <b>Flask</b>: microframework.<br>
&nbsp;- <b>flask_script</b>: To help write external scripts(eg: migrate,init,upgrade).<br>
&nbsp;- <b>flask_migrate</b>: To make system migrations.<br>
&nbsp;- <b>flask_sqlalchemy</b>: Flask's wrapper for SqlAlchemy toolkit.<br>
&nbsp;- <b>flask_modus</b>: To handle method overrides.<br>
&nbsp;- <b>flask_wtf</b>: Flask's form.<br>
&nbsp;- <b>wtforms</b>

## Application
<b>--manage.py</b><br>
&nbsp;manage.py allows to make migrations in the application, helps access the applications and databases using external scripts. This can be used for testing purposes.<br>
&nbsp;&nbsp;<b>Commands to run</b><br>
&nbsp;&nbsp;&nbsp;- <b>Signzy$</b>python manage.py db init<br>
&nbsp;&nbsp;&nbsp;&nbsp; Creates the database.<br>

&nbsp;&nbsp;&nbsp;- <b>Signzy$</b>python manage.py db migrate -m 'comments'<br>
&nbsp;&nbsp;&nbsp;&nbsp; Creates the tables in the database based on the schema present in <b>Signzy/project/models.py</b>.<br>


&nbsp;&nbsp;&nbsp;- <b>Signzy$</b>python manage.py db upgrade<br>
&nbsp;&nbsp;&nbsp;&nbsp; Creates the database file in <b>Signzy/project/</b>.<br><br>
  
<b>--Signzy/project/models.py</b><br>
can be understood as the schema for the tables in the database. Currently has two tables <b>Devices</b> and <b>Actions</b>, new tables can easily be added in this file. If a new column or table is added in the database.<br>
&nbsp; <b>Signzy$</b>python manage.py db migrate -m 'comments'<br>
&nbsp; <b>Signzy$</b>python manage.py db upgrade<br><br>

<b>--app.py</b><br>
Runs the application<br>
&nbsp;<b>Signzy$</b>python app.py<br>
&nbsp;The application will be running on the url mentioned in the file(https://127.0.0.1:5000/ as of now).<br><br>

<b>--Signzy/project/__init__.py</b><br>
Creates the database and other configurations like registering the blueprints of the resources.<br>

<b>--Signzy/project/</b> consists of two folders called <b>devices</b> and <b>actions</b>, these are the resources or modules of the application. New modules can be added by following the file structure present in other modules.<br>


<b>RESOURCES:</b><br>
<b>Signzy/project/devices/</b> has the files <b>views.py</b> which has the APIs related to devices and <b>forms.py</b> has various form validation techniques for the forms pertaining to these APIs and csrf token retention techniques which makes the forms secure.<br>
<b>devices/templates/devices</b> has the html files for these APIs.<br>


<b>Signzy/project/actions/</b> has the files <b>views.py</b> which has the APIs related to devices and <b>forms.py</b> has various form validation techniques for the forms pertaining to these APIs and csrf token retention techniques which makes the forms secure.<br>
<b>devices/templates/actions</b> has the html files for these APIs.<br>