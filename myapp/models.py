import sys
sys.path.append("..")
from app import db

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'useexisting': True}

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(64))

    def __init__(self,email,username,password_hash):
        self.email = email
        self.username = username
        self.password_hash = password_hash

    def __repr__(self):
        return '<User %r>' % self.username

class UserProfile(db.Model):
    __tablename__ = 'userprofile'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True)
    userimage = db.Column(db.String(64))

    def __init__(self, userName, userImage):
        self.username = username
        self.userimage = userimage
    def __repr__(self):
        return '<UserProfile %r>' % self.username


