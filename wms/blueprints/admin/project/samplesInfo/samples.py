from flask import Blueprint,request, render_template
from wms.forms.sample import FormQuery, FormEidt

samples_bp = Blueprint('samples',__name__)

@samples_bp.context_processor
def navInfo():
    firstnav='projectnav'
    secondnav='samplesInfo'
    pageTitle='样本信息'
    return dict(firstnav=firstnav,secondnav=secondnav,pageTitle=pageTitle)

@samples_bp.route('/samplesList',methods=['GET','POST'])
def samplesList():
    form = FormQuery()
    if request.method =='POST':
        if form.validate():
            mess = '查询成功'
            return render_template('admin/project/samplesInfo/samplesList.html',form = form,mess =mess)
        else:
            mess = '查询失败'
            return render_template('admin/project/samplesInfo/samplesList.html',form = form,mess =mess)   
    mess=''
    return render_template('admin/project/samplesInfo/samplesList.html',form = form,mess =mess)

@samples_bp.route('/samplesAdd')
def samplesAdd():
    mess= ''
    return render_template('admin/project/samplesInfo/samplesAdd.html', mess = mess)

@samples_bp.route('/samplesEdit',methods=['GET','POST'])
def samplesEdit():
    mess = ''
    form = FormEidt()
    if request.method =='POST':
        if form.validate():
            mess = '修改成功'
            return render_template('admin/project/samplesInfo/samplesEdit.html',form = form,mess =mess)
        else:
            mess = '修改失败'
            return render_template('admin/project/samplesInfo/samplesEdit.html',form = form,mess =mess)   
    mess=''
    return render_template('admin/project/samplesInfo/samplesEdit.html',form = form,mess =mess)