from flask import render_template,request,redirect,url_for
from . import main


from flask import render_template, request, redirect, url_for, abort
from ..models import User,Role,Pitch,Comment
from .forms import UpdateProfile, CreatePitchs, CommentForm
from .. import db
from flask_login import login_required, current_user
import markdown2



@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'pitch'
    pitch = Pitch.query.all()
    return render_template('index.html', title=title, pitch=pitch)

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


@main.route('/pitch', methods=['GET', 'POST'])
def create_pitchs():
    form = CreatePitchs()
    if form.validate_on_submit():

        pitch = form.pitch.data

        new_pitch = Pitch(pitch=pitch, user_id=current_user.id)

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

        new_comment = Comment(comment=comment, pitch_id=id,user_id=current_user.id)
        db.session.add(new_comment)
        db.session.commit()

    comment = Comment.query.filter_by(pitch_id=id).all()

    return render_template('comment.html', comment=comment, form=form)
