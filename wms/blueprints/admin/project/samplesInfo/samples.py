from flask import Blueprint,request, render_template,redirect,url_for
from wms.forms.sample import FormQuery, FormEidt
from wms.models.sample import Sample
from wms.extension import db

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
    page = request.args.get('page', 1, type=int)
    per_page =10
    pagination =Sample.query.paginate(page,per_page)
    mess=''
    return render_template('admin/project/samplesInfo/samplesList.html',form = form,pagination=pagination)

@samples_bp.route('/samplesAdd')
def samplesAdd():
    mess= ''
    return render_template('admin/project/samplesInfo/samplesAdd.html', mess = mess)


@samples_bp.route('/samplesDel/')
def samplesDel():
    id = request.args.get('id', 0, type=int)
    if id != '0' :
        admin = Sample.query.get(id)
        db.session.delete(admin)
        db.session.commit()
    return redirect(url_for('samples.samplesList'))


@samples_bp.route('/samplesEdit',methods=['GET','POST'])
def samplesEdit():
    mess = ''
    form = FormEidt()
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
            sample.species = form.sampleType.data
            sample.seqDose = form.seqDose.data
            sample.indexItem = form.indexItem.data
            sample.indexForward = form.indexForward.data
            sample.extractStatus = form.extractStatus.data
            sample.seqTimes = form.seqTimes.data
            sample.chartName = form.chartName.data
            sample.remark = form.remark.data
            db.session.commit()
            mess = '修改成功'
            return render_template('admin/project/samplesInfo/samplesEdit.html',form = form,mess =mess)
        else:
            mess = '修改失败'
            return render_template('admin/project/samplesInfo/samplesEdit.html',form = form,mess =mess)   
    mess=''
    return render_template('admin/project/samplesInfo/samplesEdit.html',form = form,mess =mess)