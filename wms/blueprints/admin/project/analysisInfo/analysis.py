from flask import Blueprint,render_template, request,redirect,url_for
from flask import session, flash
from wms.forms.analysis import AnalysisForm
from wms.forms.project import ProjectLogForm
from wms.models.analysis import Analysis
from wms.models.sample import Sample
from wms.models.project import Project, ProjectLog
from wms.extension import db
from flask_login import login_required
import time

analysis_bp = Blueprint('analysis',__name__)

@analysis_bp.context_processor
def navInfo():
    firstnav='projectnav'
    secondnav='analysisInfo'
    pageTitle='分析信息'
    return dict(firstnav=firstnav,secondnav=secondnav,pageTitle=pageTitle)

@analysis_bp.before_request
@login_required
def login_protect():
    pass

@analysis_bp.before_request
def initInfo():
    projectId = request.args.get('projectId', 'empty', type=str )
    if projectId != 'empty':
        session['projectId'] = projectId
        project = Project.query.get(int(projectId))
        session['projectItem'] = project.itemNumber
    elif projectId == 'clear':
        session['projectId'] = '0'


@analysis_bp.route('/addProjectLog',methods=['POST']  )
def ProjectLogAdd():
    form = ProjectLogForm()
    if form.validate and request.method == 'POST':
        project = Project.query.get(int( session.get('projectId') ) )
        localTime =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        Log = ProjectLog()
        Log.addTime = localTime
        Log.text = form.text.data
        print(Log.text)
        project.logs.append(Log)
        db.session.commit()
        flash("日志添加成功")
    else:
        flash("日志添加失败")
    return redirect(url_for('analysis.analysisList'))



@analysis_bp.route('/analysisList',methods=['GET','POST'])
def analysisList():
    form = AnalysisForm()
    logform = ProjectLogForm()
    if request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        projectId = int(session.get('projectId'))
        per_page =40
        if projectId != 0:
            project = Project.query.get(projectId)
            client = project.client
            session['clientOrg'] = client.organization
            session['clientName'] = client.name
            pagination = Analysis.query.filter(Analysis.projects_id == projectId ).paginate(page,per_page)
        else:
            return redirect(url_for('project.projectList'))
        #pagination = Analysis.query.paginate(page,per_page)
        samplesPagination = Sample.query.filter(Sample.projects_id == projectId).paginate(page,per_page)
        projectLogs = ProjectLog.query.filter( ProjectLog.projects_id == projectId).order_by(ProjectLog.id)
        #samplesPagination = Sample.query.paginate(page,per_page)
        return render_template('admin/project/analysisInfo/analysisList.html',form = form,pagination = pagination, samplesPagination = samplesPagination, project = project, client = client, projectLogs = projectLogs, logform = logform )
    return render_template('admin/project/analysisInfo/analysisList.html',form = form)

@analysis_bp.route('/analysisEdit',methods=['GET','POST'])
def analysisEdit():
    form = AnalysisForm()
    if request.method == 'GET':
        id = request.args.get('id',0,type=int)
        analysis = Analysis.query.get(id)
        form.analysisId.data = id
        form.cGroupName.data = analysis.CGroupName
        form.cSamples.data = analysis.Csamples
        form.eGroupName.data = analysis.EGroupName
        form.eSamples.data = analysis.Esamples
        return render_template('admin/project/analysisInfo/analysisEdit.html',form = form)
    if request.method == 'POST':
        if form.validate:
            id = form.analysisId.data
            analsysis = Analysis.query.get(id)
            analsysis.CGroupName = form.cGroupName.data
            analsysis.Csamples = form.cSamples.data
            analsysis.EGroupName = form.eGroupName.data
            analsysis.Esamples = form.eSamples.data
            db.session.commit()
            mess = '修改成功'
    return redirect(url_for('analysis.analysisList'))

@analysis_bp.route('/analysisDel/')
def analysisDel():
    id = request.args.get('id', 0, type=int)
    if id != '0' :
        admin = Analysis.query.get(id)
        db.session.delete(admin)
        db.session.commit()
    return redirect(url_for('analysis.analysisList'))


@analysis_bp.route('/analysisAdd',methods=['GET','POST'])
def analysisAdd():
    form = AnalysisForm()
    if request.method == 'POST':
        if form.validate:
            projectId = int(session.get('projectId'))
            print(projectId)
            if projectId != 0 :
                project = Project.query.get(projectId)
            else:
                return redirect(url_for('project.projectList'))
            analysis = Analysis()
            analysis.CGroupName = form.cGroupName.data
            analysis.Csamples = form.cSamples.data
            analysis.EGroupName = form.eGroupName.data
            analysis.Esamples = form.eSamples.data
            project.analysis.append(analysis)
            db.session.commit()
            mess = '添加成功'
            return  redirect(url_for('analysis.analysisList'))
        mess ='添加失败'
    return  redirect(url_for('analysis.analysisList'))

