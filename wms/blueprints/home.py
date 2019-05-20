from flask import Blueprint, request ,flash
from flask import render_template, redirect, url_for
from wms.forms.index import LoginForm
from flask_login import login_user, current_user, logout_user
from wms.models.admin import Admin

home_bp = Blueprint('index', __name__)


@home_bp.route('/')
def index():    
    return redirect(url_for('index.login'))


@home_bp.route('/test')
def test():
    form = LoginForm()
    return render_template('test.html', form=form)


@home_bp.route('/basic', methods=['GET', 'POST'])
def basic():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        f = form.filename.data
        username = f.filename
        print(username)
        f.save(username)
        return render_template('message.html',message= username)
    message = form.password.errors
    return render_template('message.html',message=message)


@home_bp.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    pageTitle = '登录界面'
    if request.method == 'POST' and form.validate():
        if current_user.is_authenticated:
            flash('你已经登录')
            return redirect(url_for('client.clientList'))
        username = form.userName.data
        password = form.passWord.data
        admin = Admin.query.filter(Admin.name == str(username) ).first()
        if admin:
            if username == admin.name and admin.validate_password(password):
                login_user(admin)
                flash('登录成功')
                return redirect(url_for('client.clientList'))
        else:
            flash('登录失败')
            return render_template('login.html', form = form, pageTitle =pageTitle )
    return render_template('login.html', form = form, pageTitle =pageTitle )


@home_bp.route('/logout')
def logout():
    logout_user()
    return redirect( url_for('index.login'))
