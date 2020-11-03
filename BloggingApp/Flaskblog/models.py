from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin
import secrets
class Group(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(10000000000000000000000))
    group_id = db.Column(db.String(50), default=str(secrets.token_hex(8)))
    members = db.relationship('User', backref='member', lazy=True)
    def __repr__(self):
        return (f"<Group>{self.id}")
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    image_file = db.Column(db.Text, nullable=False, default='default.jpg')
    group = db.Column(db.Integer, db.ForeignKey('group.id'))
    posts = db.relationship('Post', backref='author', lazy=True)
    joined_group = db.Column(db.Integer())
    def __repr__(self):
        return f"User('{self.id}', '{self.image_file}')"
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10000000000000000000000), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    group_id = db.Column(db.Integer)
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted})"

"""
186 museums
Monarch Butterfly migration
"""