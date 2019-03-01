from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


# class ReviewForm(FlaskForm):

#  title = StringField('Review title', validators=[Required()])

#  review = TextAreaField('Pitch review')
 

#  submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):

    submit = SubmitField('Submit')


class CreatePitchs(FlaskForm):
    pitch = TextAreaField('describe your business', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('leave The The Comment', validators=[Required()])
    submit = SubmitField('Submit')
