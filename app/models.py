from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from . import db
from flask_login import UserMixin

''''@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))'''

#Creating table that holds information
class Blogpost(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    content = db.Column(db.String(500))
    date_posted = db.Column(db.DateTime)

#Creating table that holds information
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(10))
    password = db.Column(db.String(20))
    password = db.Column(db.String(20))

# class Comment(db.Model):
#     comments_list=[]
#     __tablename__ = 'comments'

#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255),index = True)
#     email = db.Column(db.String(255),index = True)
#     blogpost_id = db.Column(db.Integer,db.ForeignKey('blogpost.id'))
#     commenter_id = db.Column(db.Integer,db.ForeignKey('users.id'))
#     comment_itself=db.Column(db.String(255),index = True)
#     posted = db.Column(db.DateTime,default=datetime.utcnow)

    def __init__(self,name,comment_itself,blog):
        self.name = name
        self.comment_itself = comment_itself
        self.blog = blog

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_blog_comments(cls,blog_id):
        comments = Comment.query.filter_by(blog_id=blog_id).all()

        return comments
    
    @classmethod
    def delete_all_blogs(cls):
        Blog.all_blogs.delete()


class Subscribe(db.Model):
    __tablename__='subscribe'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    email=db.Column(db.String(255),unique = True,index = True, nullable=False)

    def __repr__(self):
        return f'{self.email}'



