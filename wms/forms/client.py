from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,BooleanField,RadioField
from wtforms.validators import DataRequired,length,Email

class ClientForm(FlaskForm):
    userName = StringField("姓名", validators=[DataRequired()], render_kw={'placeholder':'请输入姓名',})
    gender = RadioField("性别",choices=[('1','男'),('2','女')],default='1')
    organization = StringField("单位",render_kw={'placeholder':'请输入单位名称'})
    email = StringField("电子邮箱",validators=[Email()],render_kw={'placeholder':'请输入电子邮箱',})
    telephone = StringField('电话',render_kw={'placeholder':'请输入电话号码',})
    address = StringField("通讯地址",render_kw={'placeholder':'请输入通讯地址',})
    remark = StringField('备注信息')
    submit = SubmitField("确认添加")

class ClientQuery(FlaskForm):
    userName = StringField("姓名", render_kw={'placeholder':'姓名',})
    organization = StringField("单位",render_kw={'placeholder':'单位名称'})
    email = StringField("电子邮箱",render_kw={'placeholder':'电子邮箱',})
    telephone = StringField('电话',render_kw={'placeholder':'电话号码',})
    address = StringField("通讯地址",render_kw={'placeholder':'通讯地址',})
    submit = SubmitField("搜索")