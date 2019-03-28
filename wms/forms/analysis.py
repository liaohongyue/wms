from flask_wtf import FlaskForm
from  wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class FormAdd(FlaskForm):
    cGroupName = StringField('对照组组名',validators=[DataRequired()])
    cSamples = StringField('对照组样本',validators=[DataRequired()])
    eGroupName = StringField('实验组组名',validators=[DataRequired()])
    eSamples = StringField('实验组样本',validators=[DataRequired()])
    submit = SubmitField('添加')