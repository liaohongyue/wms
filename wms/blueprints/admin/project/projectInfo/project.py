from flask import Blueprint, request
from flask import render_template
from wms.forms.project import FormAdd, FormQuery

project_bp = Blueprint('project',__name__)

@project_bp.route('/projectList')
def projectList():
    form = FormQuery()
    return render_template('admin/project/projectInfo/projectList.html',form = form)

@project_bp.route('/projectAdd',methods=['GET','POST'])
def projectAdd():
    form = FormAdd()
    if request.method =='POST' and form.validate():
        mess = '提交成功'
        return render_template('admin/project/projectInfo/projectAdd.html',firstnav="projectnav",secondnav="projectInfo",form = form,mess = mess)
    mess =  "提交失败"
    return render_template('admin/project/projectInfo/projectAdd.html',firstnav="projectnav",secondnav="projectInfo",form = form,mess = mess)