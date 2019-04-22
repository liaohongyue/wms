from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField, TextAreaField
from wtforms.validators import length, DataRequired

class SampleQueryForm(FlaskForm):
    sampleSearch = StringField("搜索",render_kw={'placeholder':'关键字',})
    submit = SubmitField("搜索")

class SampleEidtForm(FlaskForm):
    sampleId = IntegerField('id')
    amogeneItem = StringField("爱默基因编号",validators=[DataRequired()],render_kw={'placeholder':'爱默基因编号',})
    species = StringField("物种",render_kw={'placeholder':'物种',})
    libraryType =StringField("建库类型",render_kw={'placeholder':'建库类型',})
    seqType = StringField('测序类型',render_kw={'placeholder':'测序类型'})
    indexItem =StringField('index编号',render_kw={'placeholder':'index编号'})
    indexForward = StringField('index正向序列',render_kw={'placeholder':'index正向序列'})
    extractStatus = StringField('RNA提取情况', render_kw={'placeholder':'提取情况'})
    seqTimes =StringField('测序次数',render_kw={'placeholder':'测序次数',})
    seqDose= StringField('测序量',render_kw={'placeholder':'测序量'})
    sampleType = StringField('样本类型',render_kw={'placeholder':'样本类型',})
    chartName = StringField('图表名称',render_kw={'placeholder':'图表名称'})
    remark = StringField('备注',render_kw={'placeholder':'备注信息'})
    submit = SubmitField("确认修改")

class SampleAddForm(FlaskForm):
    itemNumber = StringField("项目编号",validators=[DataRequired()])
    samples = TextAreaField("样品信息",render_kw={'placeholder':'按格式要求输入样品信息，制表符分隔','rows':'10','id':'SamplesArea'})
    submit = SubmitField("提交数据")