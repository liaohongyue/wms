from flask import Blueprint, request
from flask import render_template
from wms.forms.project import FormAdd, FormQuery

project_bp = Blueprint('project',__name__)

@project_bp.context_processor
def navInfo():
    firstnav='projectnav'
    secondnav='projectInfo'
    pageTitle ='项目信息'
    return dict(firstnav=firstnav,secondnav=secondnav, pageTitle= pageTitle)

@project_bp.route('/projectList')
def projectList():
    form = FormQuery()
    mess =''
    return render_template('admin/project/projectInfo/projectList.html',form = form, mess =mess)

@project_bp.route('/projectAdd',methods=['GET','POST'])
def projectAdd():
    form = FormAdd()
    if request.method =='POST':
        if form.validate():
            mess = '提交成功'
            return render_template('admin/project/projectInfo/projectAdd.html',form = form,mess = mess)
        else:
            mess =  form.samples.data
            return render_template('admin/project/projectInfo/projectAdd.html',form = form,mess = mess)
    mess =  ""
    return render_template('admin/project/projectInfo/projectAdd.html',form = form,mess = mess)