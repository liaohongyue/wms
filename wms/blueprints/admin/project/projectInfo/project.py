from flask import Blueprint, request, redirect, url_for
from flask import render_template
from wms.forms.project import FormAdd, FormQuery, FormEdit
from wms.models.sample import Sample
from wms.models.project import Project
from wms.extension import db

project_bp = Blueprint('project',__name__)

@project_bp.context_processor
def navInfo():
    firstnav='projectnav'
    secondnav='projectInfo'
    pageTitle ='项目信息'
    return dict(firstnav=firstnav,secondnav=secondnav, pageTitle= pageTitle)

@project_bp.route('/projectEdit',methods=['GET','POST'])
def projectEdit():
    form = FormEdit()
    if request.method == 'GET':
        id = request.args.get('id', 0 ,type = int)
        if id != 0 :
            project = Project.query.get(id)
            form.projectId.data = id
            form.itemNumber.data = project.ItemNumber
            form.remark.data = project.remark
            return render_template('admin/project/projectInfo/projectEdit.html',form = form)
    if request.method == 'POST':
        if form.validate:
            id = form.projectId.data
            project = Project.query.get(id)
            project.ItemNumber = form.itemNumber.data
            project.remark = form.remark.data
            print(project.ItemNumber )
            print(project.remark)
            db.session.commit()
            mess = '修改成功'
            return render_template('admin/project/projectInfo/projectEdit.html',form = form, mess = mess)
    mess = '修改失败'
    return render_template('admin/project/projectInfo/projectEdit.html',form = form, mess = mess)

@project_bp.route('/projectList',methods=['GET','POST'])
def projectList():
    form = FormQuery()
    mess =''
    if request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        per_page =10
        pagination =Project.query.paginate(page,per_page)
    return render_template('admin/project/projectInfo/projectList.html',form = form, mess =mess,pagination = pagination)

@project_bp.route('/projectDel/')
def projectDel():
    id = request.args.get('id', 0, type=int)
    if id != '0' :
        admin = Project.query.get(id)
        db.session.delete(admin)
        db.session.commit()
    return redirect(url_for('project.projectList'))


@project_bp.route('/projectAdd',methods=['GET','POST'])
def projectAdd():
    form = FormAdd()
    if request.method =='POST':
        if form.validate:
            project = Project()
            project.ItemNumber = form.itemNumber.data
            db.session.add(project)
            db.session.commit()
            samples = form.samples.data
            samples = samples.split(sep='\n')
            for sample in samples:
                sampleInfo = Sample() # 初始化模型
                if sample == '':continue #判断输入数据
                sample = sample.split(sep='\t')
                if sample[0] == '':continue
                sampleInfo.amogeneItem  = sample[0]
                sampleInfo.libraryType  = sample[1]
                sampleInfo.seqType  = sample[2]
                sampleInfo.sampleType = sample[3]
                sampleInfo.species = sample[4]
                sampleInfo.seqDose  = sample[5]
                sampleInfo.indexItem = sample[6]
                sampleInfo.indexForward = sample[7]
                sampleInfo.extractStatus = sample[8]
                sampleInfo.seqTimes = sample[9]
                sampleInfo.chartName = sample[10]
                db.session.add(sampleInfo)
                db.session.commit()
            mess = '添加成功'
            return render_template('admin/project/projectInfo/projectAdd.html',form = form,mess = mess)
        else:
            mess =  form.samples.data
            return render_template('admin/project/projectInfo/projectAdd.html',form = form,mess = mess)
    mess =  ""
    return render_template('admin/project/projectInfo/projectAdd.html',form = form,mess = mess)