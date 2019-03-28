from flask import Blueprint,request, render_template
from wms.forms.sample import FormQuery

samples_bp = Blueprint('samples',__name__)

@samples_bp.route('/samplesList',methods=['GET','POST'])
def samplesList():
    form = FormQuery()
    mess =''
    return render_template('admin/project/samplesInfo/samplesList.html',form = form, mess = mess)

@samples_bp.route('/samplesAdd')
def samplesAdd():
    return render_template('admin/project/samplesInfo/samplesAdd.html')

@samples_bp.route('/samplesEdit')
def samplesEdit():
    return render_template('admin/project/samplesInfo/samplesEdit.html')