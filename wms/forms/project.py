from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField, IntegerField,DateField
from wtforms.validators import length,DataRequired

class ProjectForm(FlaskForm):
    projectId = IntegerField('id')
    clientId = StringField('客户ID号')
    itemNumber = StringField("项目编号",validators=[DataRequired()])
    samplesDate = DateField("样品接收日期")
    createLib = StringField("建库人")
    checkoutLib = StringField("是否库检")
    isSettle =   StringField("是否结算")
    amogeneSettle = StringField("结算金额 （元） 爱默核对:")
    novoStage = StringField("诺和分期号")
    novoSettle = StringField("诺和结算金额（元）:")
    isReleaseData = StringField("是否释放数据")
    period = StringField("实验周期")
    samples = TextAreaField("样品信息",render_kw={'placeholder':'按格式要求输入样品信息，制表符分隔','rows':'10','id':'SamplesArea'})
    remark = TextAreaField("备注信息",render_kw={'placeholder':'这里输入一些项目备注信息','rows':'5','id':'remarkInfo'})
    submit = SubmitField("提交数据")

class FormQuery(FlaskForm):
    itemNumber = StringField("筛选条件", render_kw={'placeholder':'项目编号'} )
    submit = SubmitField("搜索")
