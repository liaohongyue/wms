from flask import Blueprint,render_template, request
from wms.forms.analysis import FormAdd

analysis_bp = Blueprint('analysis',__name__)

@analysis_bp.route('/analysisList',methods=['GET','POST'])
def analysisList():
    form = FormAdd()
    mess = ''
    return render_template('admin/project/analysisInfo/analysisList.html',form = form, mess=mess)

@analysis_bp.route('/analysisEdit')
def analysisEdit():
    form = FormAdd()
    mess = ''
    return render_template('admin/project/analysisInfo/analysisEdit.html',form = form,mess=mess)