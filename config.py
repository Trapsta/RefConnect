#config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dont-even-try'

OAUTH_CREDENTIALS = {
	'facebook' : {
		'id' : '1629151060715822',
		'secret' : '36ca234ee9c726e680d8a54b4981f9de'
	},
	'twitter' : {
		'id' : 'KX3jsjQpseMJm3LNDY4q2zdt9',
		'secret' : 'tSKxdeJaLAN6p052G7vq7AwtebEO3A8oxw7UczICr8er3vBERv'
	}
}