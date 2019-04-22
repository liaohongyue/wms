from flask_wtf import FlaskForm
from  wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired

class AnalysisForm(FlaskForm):
    analysisId = IntegerField('id')
    cGroupName = StringField('对照组组名',validators=[DataRequired()])
    cSamples = StringField('对照组样本',validators=[DataRequired()])
    eGroupName = StringField('实验组组名',validators=[DataRequired()])
    eSamples = StringField('实验组样本',validators=[DataRequired()])
    submit = SubmitField('提交')