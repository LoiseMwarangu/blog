#Importing flask and render_template
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from . import main
from ..models import Blogpost 
from ..request import random_quote
from .forms import SubscribeForm
#Importing Flask-SQLAlchemy for database setup.
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required
from .. import db
#Route for index...views
@main.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    myquote= random_quote()
    quote = myquote["quote"]
    quote_author = myquote ["author"]
    return render_template('index.html', posts=posts, quote= quote, quote_author= quote_author)

#Route for about
@main.route('/about')
def about():
    return render_template('about.html')

#Route for post
@main.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()


    return render_template('post.html', post= post )

#Route for add
@main.route('/add')
def add():
    return render_template('add.html')

#Route for Adding Post
@main.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author,content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()


    return redirect(url_for('main.index'))
@main.route('/subscribe',methods=["GET","POST"])
def subscribe():
    form=SubscribeForm()

    if form.validate_on_submit():
        subscriber = Subscribe(email=form.email.data)

        db.session.add(subscriber)
        db.session.commit()

        # mail_message("Welcome to The Home of Awesome Blogs","email/subscribe_user",subscriber.email,subscriber=subscriber)
        # flash('A subscription confirmation has been sent to you via email')

        return redirect(url_for('main.index'))

        title = 'Subscribe Now'

    return render_template('subscribe.html',subscribe_form = form)