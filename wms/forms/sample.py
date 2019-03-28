from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import length, DataRequired

class FormQuery(FlaskForm):
    amogeneItem = StringField("爱默基因编号",render_kw={'placeholder':'爱默基因编号',})
    libraryType =StringField("建库类型",render_kw={'placeholder':'建库类型',})
    sampleType = StringField('样本类型',render_kw={'placeholder':'样本类型',})
    species = StringField("物种",render_kw={'placeholder':'物种',})
    seqTimes =StringField('测序次数',render_kw={'placeholder':'测序次数',})
    submit = SubmitField("搜索")
