from app import app
from flask import render_template

@app.route('/')
def index():
	user = {'username': 'Jasper'}
	return render_template('index.html',
		title='Welcome to RefConnect')