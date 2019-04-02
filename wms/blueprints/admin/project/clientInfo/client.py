from flask import Blueprint
from flask import render_template, redirect, url_for ,request
from wms.forms.client import ClientForm,ClientQuery
from wms.models.client import Client
from wms.extension import db
from faker import Faker

client_bp = Blueprint('client',__name__)

@client_bp.context_processor
def navInfo():
    firstnav='projectnav'
    secondnav='clientInfo'
    pageTitle='客户信息'
    return dict(firstnav=firstnav,secondnav=secondnav,pageTitle=pageTitle)


@client_bp.route('/clientDel/')
def ClientDel():
    id = request.args.get('id', 0, type=int)
    if id != '0' :
        client = Client.query.get(id)
        db.session.delete(client)
        db.session.commit()
    return redirect(url_for('client.clientlist'))


@client_bp.route('/clientList')
def clientlist():
    form = ClientForm()
    formquery = ClientQuery()
    page = request.args.get('page', 1, type=int)
    per_page =10
    pagination = Client.query.paginate(page,per_page)
    return render_template('admin/project/clientInfo/clientList.html',form = form,formq=formquery,pagination= pagination )

@client_bp.route('/clientEdit', methods=['GET','POST'])
def clientEdit():
    form = ClientForm()
    if request.method == 'GET':
        id = request.args.get('id', 0, type=int)
        client = Client.query.get(id)
        form.clientId.data = id
        form.userName.data = client.name
        if client.gender == '男':
            form.gender.data ='1'
        else:
            form.gender.data ='2'
        form.organization.data = client.organization
        form.telephone.data = client.telephone
        form.email.data = client.email
        form.address.data = client.address
        form.remark.data = client.remark
        return render_template('admin/project/clientInfo/clientEdit.html',form = form)

    if request.method == 'POST':
        if form.validate:
            id = form.clientId.data
            client = Client.query.get(id)
            client.name = form.userName.data
            client.organization = form.organization.data
            if form.gender.data == '1':
                client.gender = '男'
            else:
                client.gender = '女'
            client.email = form.email.data
            client.telephone = form.telephone.data
            client.address = form.address.data
            client.remark = form.remark.data
            db.session.commit()
            mess = '修改成功'
            return render_template('admin/project/clientInfo/clientEdit.html',form = form,mess = mess)
        mess = '修改失败'
    return render_template('admin/project/clientInfo/clientEdit.html',form = form,mess = mess)

@client_bp.route('/clientAdd', methods=['GET','POST'])
def clientAdd():
    form = ClientForm()
    formquery = ClientQuery()
    if request.method =='POST': 
        if form.validate:
            client = Client()
            client.name = form.userName.data
            if form.gender.data == '1':
                client.gender= '男'
            else:
                client.gender ='女'
            client.organization = form.organization.data
            client.telephone = form.telephone.data
            client.email = form.email.data
            client.address = form.address.data
            client.remark = form.remark.data
            db.session.add(client)
            db.session.commit()
            #===========================
            # for i in range(300):
            #     fake = Faker(locale='zh_CN')
            #     info = fake.profile(fields=None, sex=None)
            #     client = Client()
            #     client.name = info['name']
            #     if info['sex'] == 'F':
            #         client.gender= '男'
            #     else:
            #         client.gender ='女'
            #     client.organization = info['company']
            #     client.telephone = fake.phone_number()
            #     client.email = info['mail']
            #     client.address = info['address']
            #     client.remark = info['job']
            #     db.session.add(client)
            #     db.session.commit()
            mess ='客户:  ' + client.name + ' 添加成功'
            return render_template('admin/project/clientInfo/clientList.html',form = form,formq=formquery,mess=mess)
        else:
            mess = "添加失败，请验证数据正确"
            return render_template('admin/project/clientInfo/clientList.html',form = form,formq=formquery,mess=mess)
    mess = "添加失败，请却数据正确"
    return render_template('admin/project/clientInfo/clientList.html',form = form,formq=formquery,mess=mess)

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

