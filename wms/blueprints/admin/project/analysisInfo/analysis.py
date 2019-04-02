from flask import Blueprint,render_template, request,redirect,url_for
from wms.forms.analysis import FormAdd
from wms.models.analysis import Analysis
from wms.models.sample import Sample
from wms.extension import db

analysis_bp = Blueprint('analysis',__name__)

@analysis_bp.context_processor
def navInfo():
    firstnav='projectnav'
    secondnav='analysisInfo'
    pageTitle='分析信息'
    return dict(firstnav=firstnav,secondnav=secondnav,pageTitle=pageTitle)

@analysis_bp.route('/analysisList',methods=['GET','POST'])
def analysisList():
    form = FormAdd()
    if request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        per_page =40
        pagination = Analysis.query.paginate(page,per_page)
        samplesPagination = Sample.query.paginate(page,per_page)
        return render_template('admin/project/analysisInfo/analysisList.html',form = form,pagination = pagination, samplesPagination = samplesPagination)
    mess = ''
    return render_template('admin/project/analysisInfo/analysisList.html',form = form, mess=mess)

@analysis_bp.route('/analysisEdit',methods=['GET','POST'])
def analysisEdit():
    form = FormAdd()
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
    form = FormAdd()
    mess =''
    if request.method == 'POST':
        if form.validate:
            analysis = Analysis()
            analysis.CGroupName = form.cGroupName.data
            analysis.Csamples = form.cSamples.data
            analysis.EGroupName = form.eGroupName.data
            analysis.Esamples = form.eSamples.data
            db.session.add(analysis)
            db.session.commit()
            mess = '添加成功'
            return  redirect(url_for('analysis.analysisList'))
        mess ='添加失败'
    return  redirect(url_for('analysis.analysisList'))

