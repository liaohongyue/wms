from flask import Blueprint,request, render_template,redirect,url_for,session
from wms.forms.sample import SampleEidtForm, SampleQueryForm, SampleAddForm
from sqlalchemy import or_
from wms.models.sample import Sample
from wms.models.project import Project
from wms.extension import db
from flask_login import login_required

samples_bp = Blueprint('samples',__name__)

@samples_bp.before_request
@login_required
def login_protect():
    pass

@samples_bp.context_processor
def navInfo():
    firstnav='projectnav'
    secondnav='samplesInfo'
    pageTitle='样本信息'
    return dict(firstnav=firstnav,secondnav=secondnav,pageTitle=pageTitle)

@samples_bp.route('/samplesList',methods=['GET','POST'])
def samplesList():
    mess = ''
    form = SampleQueryForm()
    page = request.args.get('page', 1, type=str)
    if page == 'clear':
        session['sampleSearch'] = None
        page='1'
    page = int(page)
    per_page =10
    if form.sampleSearch.data != None or session.get('sampleSearch') != None:
        if form.sampleSearch.data != None:
            sampleSearch = form.sampleSearch.data
            session['sampleSearch'] = sampleSearch
        elif session.get('sampleSearch') != None:
            sampleSearch = session.get('sampleSearch')
        sampleSearch = '%' + sampleSearch + '%'
        pagination = Sample.query.filter(or_( Sample.amogeneItem.like(sampleSearch),Sample.species.like(sampleSearch)  )).paginate(page,per_page)
        mess = '查询成功'
    else:
        pagination = Sample.query.paginate(page,per_page)
    return render_template('admin/project/samplesInfo/samplesList.html', form = form, pagination = pagination, mess = mess)

@samples_bp.route('/samplesAdd',methods=['GET','POST'] )
def samplesAdd():
    form = SampleAddForm()
    if request.method == 'POST':
        if form.validate:
            project = Project.query.get(form.itemNumber.data)
            samples = form.samples.data
            samples = samples.split(sep='\n')
            for sample in samples:
                sampleInfo = Sample() # 初始化模型
                if sample == '':continue #判断输入数据
                sample = sample.split(sep='\t')
                if sample[0] == '':continue
                sampleInfo.amogeneItem  = sample[0]
                if len(sample) <2  : continue
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
    form.itemNumber.data = session.get('projectId')
    return render_template('admin/project/samplesInfo/samplesAdd.html', form = form)


@samples_bp.route('/samplesDel/')
def samplesDel():
    id = request.args.get('id', 0, type=int)
    if id != '0' :
        admin = Sample.query.get(id)
        db.session.delete(admin)
        db.session.commit()
        if session.get('projectId') != None:
            print(url_for('analysis.analysisList') + "?projectId=" + session.get('projectId'))
            return  redirect(url_for('analysis.analysisList') + "?projectId=" + session.get('projectId') )
    return redirect(url_for('samples.samplesList'))


@samples_bp.route('/samplesEdit',methods=['GET','POST'])
def samplesEdit():
    mess = ''
    form = SampleEidtForm
    if request.method =='GET':
        id = request.args.get('id',0,type=int)
        sample = Sample.query.get(id)
        form.sampleId.data = id
        form.amogeneItem.data = sample.amogeneItem
        form.libraryType.data = sample.libraryType
        form.seqType.data = sample.seqType
        form.sampleType.data = sample.sampleType
        form.species.data = sample.species
        form.seqDose.data = sample.seqDose
        form.indexItem.data = sample.indexItem
        form.indexForward.data = sample.indexForward
        form.extractStatus.data = sample.extractStatus
        form.seqTimes.data = sample.seqTimes
        form.chartName.data =sample.chartName
        form.remark.data = sample.remark
        return render_template('admin/project/samplesInfo/samplesEdit.html',form = form)
    if request.method =='POST':
        if form.validate():
            id  = form.sampleId.data
            sample = Sample.query.get(id)
            sample.amogeneItem = form.amogeneItem.data
            sample.libraryType = form.libraryType.data
            sample.seqType = form.seqType.data
            sample.sampleType = form.sampleType.data
            sample.species = form.species.data
            sample.seqDose = form.seqDose.data
            sample.indexItem = form.indexItem.data
            sample.indexForward = form.indexForward.data
            sample.extractStatus = form.extractStatus.data
            sample.seqTimes = form.seqTimes.data
            sample.chartName = form.chartName.data
            sample.remark = form.remark.data
            db.session.commit()
            mess = '修改成功'
            if session.get('projectId') != None:
                return  redirect(url_for('analysis.analysisList') + "?projectId=" + session.get('projectId') )
            return render_template('admin/project/samplesInfo/samplesEdit.html',form = form,mess =mess)
        else:
            mess = '修改失败'
            return render_template('admin/project/samplesInfo/samplesEdit.html',form = form,mess =mess)   
    mess=''
    return render_template('admin/project/samplesInfo/samplesEdit.html',form = form,mess =mess)