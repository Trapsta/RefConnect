from app import db
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	social_id = db.Column(db.String(64), nullable=False, unique=True)
	username = db.Column(db.String(64), index=True, unique=True, nullable=False)
	email = db.Column(db.String(120), index=True, unique=True) #Twitter maintain integrity

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True
	

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
			try:
				return unicode(self.id)
			except NameError:
				return str(self.id)
	

	def __repr__(self):
		return '<User %r>' % (self.username)

		