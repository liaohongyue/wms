from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileRequired,FileField
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,length

class LoginForm(FlaskForm):
    filename = FileField('Upload file', validators=[FileRequired(),FileAllowed(['zip','png','jpg'])])
    username = StringField('UserName',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),length(8,128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('log in')