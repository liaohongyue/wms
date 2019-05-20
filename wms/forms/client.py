from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,BooleanField,RadioField,IntegerField
from wtforms.validators import DataRequired,length,Email

class ClientForm(FlaskForm):
    clientId = IntegerField('id')
    userName = StringField("姓名", validators=[DataRequired()], render_kw={'placeholder':'请输入姓名',},default='')
    gender = RadioField("性别",choices=[('1','男'),('2','女')],default='1')
    organization = StringField("单位",render_kw={'placeholder':'请输入单位名称'}, default='')
    email = StringField("电子邮箱",validators=[Email()],render_kw={'placeholder':'请输入电子邮箱',}, default='')
    telephone = StringField('电话',render_kw={'placeholder':'请输入电话号码',}, default='')
    address = StringField("通讯地址",render_kw={'placeholder':'请输入通讯地址',}, default='')
    remark = StringField('备注信息', default='')
    submit = SubmitField("确认")

class ClientQuery(FlaskForm):
    clientSearch = StringField("搜索内容", render_kw={'placeholder':'搜索',})
    submit = SubmitField("搜索")
