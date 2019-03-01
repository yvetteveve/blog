from flask import render_template,request,redirect,url_for
from . import main
from flask import render_template, request, redirect, url_for, abort
from ..models import User,Comment,Pitch
from .forms import UpdateProfile
from .. import db
from flask_login import login_required, current_user

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

   

    title = 'Home - Welcome to The best pitch Review Website Online'

    
    return render_template('index.html', title = title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


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

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)



@main.route('/pitch', methods=['GET', 'POST'])
def create_pitchs():
    form = CreatePitchs()
    print(current_user.id)
    if form.validate_on_submit():

        pitch = form.pitch.data

        new_pitch = Pitch(pitch=pitch, userid=current_user.id)

        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('pitch.html', form=form, user=current_user)


@main.route('/pitch/comment/<int:id>', methods=['GET', 'POST'])
@login_required
def create_comments(id):
    form = CommentForm()
   
    if form.validate_on_submit():

        comment = form.comment.data

        new_comment = Comment(comment=comment, pitchid=id,userid=current_user.id)
        db.session.add(new_comment)
        db.session.commit()
        comment = Comment.query.filter_by(pitchid=id).all()

    return render_template('comment.html', comment=comment, form=form)
