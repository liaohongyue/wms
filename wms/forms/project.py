from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import length,DataRequired

class FormAdd(FlaskForm):
    itemNumber = StringField("项目编号",validators=[DataRequired()])
    samples = TextAreaField("样品信息",render_kw={'placeholder':'按格式要求输入样品信息，制表符分隔','rows':'10','id':'SamplesArea'})
    submit = SubmitField("提交数据")

class FormQuery(FlaskForm):
    itemNumber = StringField("筛选条件", render_kw={'placeholder':'项目编号'} )
    submit = SubmitField("搜索")