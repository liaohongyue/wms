from flask import Blueprint, request, redirect, url_for
from flask import render_template, session
from wms.forms.project import FormAdd, FormQuery, FormEdit
from wms.models.sample import Sample
from wms.models.project import Project
from wms.models.client import Client
from wms.extension import db

project_bp = Blueprint('project',__name__)

@project_bp.context_processor
def navInfo():
    firstnav='projectnav'
    secondnav='projectInfo'
    pageTitle ='项目信息'
    return dict(firstnav=firstnav,secondnav=secondnav, pageTitle= pageTitle)

@project_bp.before_request
def initInfo():
    clientId = request.args.get('clientId', 'empty', type=str)
    if clientId != 'empty':
        if clientId == 'clear':
            session['clientId'] = '0'
            session['clientName'] = '所有客户'
            session['clientOrg'] = ''
        else:
            session['clientId'] = clientId
            client = Client.query.get(int(clientId))
            session['clientName'] = client.name
            session['clientOrg'] = client.organization
    

@project_bp.route('/projectEdit',methods=['GET','POST'])
def projectEdit():
    form = FormEdit()
    if request.method == 'GET':
        id = request.args.get('id', 0 ,type = int)
        if id != 0 :
            project = Project.query.get(id)
            form.projectId.data = id
            form.itemNumber.data = project.itemNumber
            form.remark.data = project.remark
            return render_template('admin/project/projectInfo/projectEdit.html',form = form)
    if request.method == 'POST':
        if form.validate:
            id = form.projectId.data
            project = Project.query.get(id)
            project.itemNumber = form.itemNumber.data
            project.remark = form.remark.data
            db.session.commit()
            mess = '修改成功'
            return render_template('admin/project/projectInfo/projectEdit.html',form = form, mess = mess)
    mess = '修改失败'
    return render_template('admin/project/projectInfo/projectEdit.html',form = form, mess = mess)

@project_bp.route('/projectList',methods=['GET','POST'])
def projectList():
    form = FormQuery()
    searchData = ''
    page = request.args.get('page', 1, type=int)
    clientId = int(session.get('clientId'))
    per_page = 5
    if form.itemNumber.data != None or session.get('projectSearchData') != None:
        if form.itemNumber.data != None:
            searchData = str(form.itemNumber.data)
            session['projectSearchData'] = searchData
        elif session.get('projectSearchData') != None:
            searchData = session.get('projectSearchData')
        searchData = '%' + searchData + '%'
    print(searchData)
    if clientId != 0:  # 指定客户id号
        pagination =  Project.query.filter(Project.client_id == clientId).paginate(page,per_page)
    elif searchData != '': # 只有搜索内容
        pagination =Project.query.filter(Project.itemNumber.like(searchData)).paginate(page,per_page)
    else: # 没有指定客户id，也没搜索内容
        pagination =Project.query.paginate(page,per_page)
    return render_template('admin/project/projectInfo/projectList.html',form = form,pagination = pagination)

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
            clientId = int(session.get('clientId'))
            client = Client.query.get(clientId)
            project = Project()
            project.itemNumber = form.itemNumber.data
            client.projects.append(project)
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
                project.samples.append(sampleInfo)
                db.session.commit()
            mess = '添加成功'
            return render_template('admin/project/projectInfo/projectAdd.html',form = form,mess = mess)
        else:
            mess =  form.samples.data
            return render_template('admin/project/projectInfo/projectAdd.html',form = form,mess = mess)
    mess =  ""
    return render_template('admin/project/projectInfo/projectAdd.html',form = form,mess = mess)