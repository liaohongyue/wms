from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired,length

class LoginForm(FlaskForm):
    userName = StringField("用户名",validators=[DataRequired()],render_kw={'placeholder':'请输入用户名','autocomplete':'off'})
    passWord = PasswordField("密码",validators=[DataRequired(),length(1,115)],render_kw={'placeholder':'请输入密码',})
    rememberMe = BooleanField("记住我")
    submit = SubmitField("登录")