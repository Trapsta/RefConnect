from flask import render_template, flash, redirect, url_for, session, request, g, current_app
from app import app, db, lm
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from rauth import OAuth1Service, OAuth2Service
from datetime import datetime
from .oauth import OAuthSignIn
from .forms import SignInForm, SignUpForm
from .models import User


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()


@app.route('/')
def index():
	user = {'username': 'Jasper'}
	return render_template('index.html',
		title='Welcome to RefConnect')

@app.route('/login', methods=['GET','POST'])
def login():
	if g.user is not None and g.user.is_authenticated:
		return redirect(url_for('index'))
	form = SignInForm()
	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		return login_user(user)
		flash('Logged in successfully.')
	return render_template('login.html',
		title='Sign In',
		form = form)

@app.route('/authorize/<provider>')
def oauth_authorize(provider):
	if not current_user.is_anonymous:
		return redirect(url_for('index'))
	oauth = OAuthSignIn.get_provider(provider)
	return oauth.authorize()

@app.route('/callback/<provider>')
def oauth_callback(provider):
	if not current_user.is_anonymous:
		return redirect(url_for('index'))
	oauth = OAuthSignIn.get_provider(provider)
	social_id, username, email = oauth.callback()
	if social_id is None:
		flash('Authenciation failed')
		return redirect(url_for('index'))
	user = User.query.filter_by(social_id=social_id).first()
	if not user:
		user = User(social_id=social_id, username=username, email=email)
		db.session.add(user)
		db.session.commit()
	login_user(user, True)
	return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignUpForm()
	return render_template('signup.html',
		title='Sign Up',
		form=form)