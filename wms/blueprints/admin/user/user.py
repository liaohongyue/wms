from flask import Blueprint, render_template,request,redirect,url_for, flash
from wms.forms.admin import AdminForm, PasswordEditForm
from wms.models.admin import Admin
from wms.extension import db
from faker import Faker
import faker
from flask import flash, session

user_bp = Blueprint('user',__name__)

@user_bp.context_processor
def navInfo():
    firstnav='usernav'
    secondnav='analysisInfo'
    pageTitle='分析信息'
    return dict(firstnav=firstnav,secondnav=secondnav,pageTitle=pageTitle)


@user_bp.route('/userList')
def userList():
    page = request.args.get('page', 1, type=int)
    per_page =10
    form = AdminForm()
    pagination = Admin.query.paginate(page,per_page)
    return render_template('admin/user/userList.html',form = form,pagination=pagination)



@user_bp.route('/userDel/')
def userDel():
    id = request.args.get('id', 0, type=int)
    if id != '0' :
        admin = Admin.query.get(id)
        db.session.delete(admin)
        db.session.commit()
    return redirect(url_for('user.userList'))

@user_bp.route('/userAdd', methods=['GET','POST'])
def userAdd():
    form = AdminForm()
    if request.method == 'POST':
        if form.validate:
            admin = Admin()
            admin.name = form.name.data
            if form.gender.data == '1':
                admin.gender="男"
            else:
                admin.gender="女"
            admin.telephone = form.telephone.data
            admin.email = form.email.data
            admin.unit = form.unit.data
            password = form.password.data
            admin.set_password(str(password))
            db.session.add(admin)
            db.session.commit()
            mess = form.name.data + "添加成功"
            return redirect(url_for('user.userList'))
        else: 
            mess = '添加失败'
            redirect(url_for('user.userList'))
    mess=''
    return redirect(url_for('user.userList'))



@user_bp.route('/userInfoEdit/', methods=['GET','POST'])
def userInfoEdit():
    form = AdminForm()
    if request.method == "GET":
        id = request.args.get('id', 0, type=int)
        admin = Admin.query.get(id)
        form.name.data = admin.name
        if admin.gender == "男":
            form.gender.data = '1'
        else:
            form.gender.data = '2'
        form.telephone.data = admin.telephone
        form.email.data = admin.email
        form.unit.data = admin.unit
        form.adminid.data = id
        mess= ''
        return render_template('admin/user/userInfoEdit.html',mess=mess,admin=admin,form=form)
    
    if request.method == 'POST' and form.validate:
        id = form.adminid.data
        admin = Admin.query.get(id)
        admin.name = form.name.data
        if form.gender.data == '1':
            admin.gender="男"
        else:
            admin.gender="女"
        admin.telephone = form.telephone.data
        admin.email = form.email.data
        admin.unit = form.unit.data
        admin.password_hash = form.password.data
        db.session.commit()
    return redirect(url_for('user.userList'))

@user_bp.route('/userPasswordEdit', methods=['POST','GET'])
def userPasswordEdit():
    form = PasswordEditForm()
    userId = session.get('user_id')
    if request.method == 'POST' and form.validate:
        oldPassword = form.oldPassword.data
        newPassword = form.newPassword.data
        userId = session.get('user_id')
        admin = Admin.query.get(int( userId))
        if admin.validate_password(oldPassword):
            admin.set_password(newPassword)
            db.session.commit()
            flash('密码 修改成功')
            return redirect( url_for('user.userPasswordEdit') )
        else:
            flash("密码 错误")
            return redirect( url_for('user.userPasswordEdit') )
    return render_template('admin/user/userPasswordEdit.html', form = form)