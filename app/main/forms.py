from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class AddPostForm(FlaskForm):
    title=StringField('Title',validators = [Required()])
    content=TextAreaField('Content',validators = [Required()])
    image=StringField('Image url',validators = [Required()])
    submit=SubmitField('SUBMIT')

class CommentForm(FlaskForm):
   
   username = StringField('Enter your name',validators=[Required()])
   comment = TextAreaField('pitch comment', validators=[Required()])
   submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class SubscriptionForm(FlaskForm):
    name=StringField('Name',validators =[Required()])
    email=StringField('Email',validators =[Required()])
    submit = SubmitField('Submit')

class UpdatePostForm(FlaskForm):
    title=StringField('Title',validators = [Required()])
    content=TextAreaField('Content',validators = [Required()])
    submit=SubmitField('SUBMIT')
