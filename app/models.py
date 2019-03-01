from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    class pitch(db.Model):
        __tablename__ = 'pitch'

      id = db.Column(db.Integer, primary_key=True)
      pitch = db.Column(db.String(255), index=True)
      user id = db.Column(db.String(255), unique=True, index=True)
      user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
      user_id = db.Column(db.Integer,db.ForeignKey("pitch.id"))

    class comment(db.Model)
     __tablename__ = 'comment'

     id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(255), index=True)
      email = db.Column(db.String(255), unique=True, index=True)
      user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    
