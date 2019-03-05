
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class Quote:
   '''
   Quote class to define quote objects
   '''

   def __init__(self,id,author,content):
     self.id=id
     self.author=author
     self.content=content
    
class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True , index=True)
    bio= db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pass_secure=db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Comment(db.Model):
    __tablename__= 'comments'
    
    id= db.Column(db.Integer,primary_key= True)
    username=db.Column(db.String(255))
    content = db.Column(db.String(255))
    
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(post_id=id).all()
        return comments

    
    def delete_comment(self):
       db.session.delete(self)
       db.session.commit()


    # @classmethod
    # def get_commentss(cls,id):
    #     comments = Comment.query.filter_by(user_id=id).all()
    #     return comments

class Post(db.Model):
    __tablename__= 'posts'
    
    id= db.Column(db.Integer,primary_key= True)
    title=db.Column(db.String(255))
    content = db.Column(db.String(500))
    image=db.Column(db.String(500))
   
    comments = db.relationship('Comment',backref='post' ,lazy='dynamic')


    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_posts(cls):
        Post.all_posts.clear()

    @classmethod
    def get_posts(cls):
        posts = Post.query.all()
        return posts

    def delete_post(self, id):
       comments = Comment.query.filter_by(id=id).all()
       for comment in comments:
         db.session.delete(comment)
         db.session.commit()
       db.session.delete(self)
       db.session.commit()

    # @classmethod
    # def get_commentss(cls,id):
    #     comments = Comment.query.filter_by(user_id=id).all()
    #     return comments



class Subscription(db.Model):
     __tablename__='subscribers'

     id=db.Column(db.Integer,primary_key=True)
     name=db.Column(db.String(255))
     email = db.Column(db.String(255),unique = True,index = True)