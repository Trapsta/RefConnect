from flask.ext.wtf import Form 
from wtforms import StringField, BooleanField,PasswordField
from wtforms.validators import DataRequired

class SignInForm(Form):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
	remember_me = BooleanField('remember_me', default=False)

class SignUpForm(Form):
	firstname = StringField('First Name', validators=[DataRequired()])
	lastname = StringField('Last Name', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	phone = StringField('Phone', validators=[DataRequired()])
		
