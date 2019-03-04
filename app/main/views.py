from flask import render_template,request,redirect,url_for
from . import main


from flask import render_template, request, redirect, url_for, abort
from ..models import User,Role,blog,Comment
from .forms import UpdateProfile, Createblogs, CommentForm
from .. import db
from flask_login import login_required, current_user
import markdown2



@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'blog'
    blog = blog.query.all()
    return render_template('index.html', title=title, blog=blog)

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()


    return render_template('profile/update.html', form=form)


@main.route('/blog', methods=['GET', 'POST'])
def create_blogs():
    form = Createblogs()
    if form.validate_on_submit():

        blog = form.blog.data

        new_blog = blog(blog=blog, user_id=current_user.id)

        db.session.add(new_blog)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('blog.html', form=form, user=current_user)


@main.route('/blog/comment/<int:id>', methods=['GET', 'POST'])
@login_required
def create_comments(id):
    form = CommentForm()
   
    if form.validate_on_submit():

        comment = form.comment.data

        new_comment = Comment(comment=comment, blog_id=id,user_id=current_user.id)
        db.session.add(new_comment)
        db.session.commit()

    comment = Comment.query.filter_by(blog_id=id).all()

    return render_template('comment.html', comment=comment, form=form)
