from flask import Blueprint
from flask import render_template, redirect, url_for ,request
from wms.forms.client import ClientForm,ClientQuery

client_bp = Blueprint('client',__name__)

@client_bp.context_processor
def navInfo():
    firstnav='projectnav'
    secondnav='clientInfo'
    pageTitle='客户信息'
    return dict(firstnav=firstnav,secondnav=secondnav,pageTitle=pageTitle)

@client_bp.route('/clientList')
def clientlist():
    form = ClientForm()
    formquery = ClientQuery()
    return render_template('admin/project/clientInfo/clientList.html',form = form,formq=formquery,mess='' )

@client_bp.route('/clientEdit')
def clientEdit():
    return render_template('admin/project/clientInfo/clientEdit.html',mess ='')

@client_bp.route('/clientAdd', methods=['GET','POST'])
def clientAdd():
    form = ClientForm()
    if request.method =='POST': 
        if form.validate():
            return redirect(url_for('project.projectList'))
        else:
            mess = "添加失败，请却数据正确"
    return render_template('admin/project/clientInfo/clientList.html',form = form,mess=mess)
    mess = "添加失败，请却数据正确"
    return render_template('admin/project/clientInfo/clientList.html',form = form,mess=mess)

@client_bp.route('/clientQuery', methods=['GET','POST'])

def clientQuery():
    formquery = ClientQuery()
    form = ClientForm()
    if request.method =='POST' and formquery.validate():
        mess = "搜索成功"
        return render_template('admin/project/clientInfo/clientList.html',form = form ,formq = formquery,mess=mess)
    # mess = "搜索失败"
    mess = ''
    return render_template('admin/project/clientInfo/clientList.html',form= form, formq= formquery,mess=mess)

