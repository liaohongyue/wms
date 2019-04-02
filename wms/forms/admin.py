from flask_wtf import FlaskForm
from  wtforms import StringField,SubmitField,RadioField,BooleanField,IntegerField
from wtforms.validators import DataRequired

class  AdminForm(FlaskForm):
    adminid = IntegerField('id')
    name = StringField('用户名',validators=[DataRequired()])
    gender = RadioField('性别',choices=[('1','男'),('2','女')],default='1')
    telephone = StringField('电话')
    email = StringField('电子邮箱')
    unit = StringField('单位')
    password = StringField('密码')
    password_enter = StringField("确认密码")
    submit = SubmitField("提交数据")