from flask import Blueprint, request ,flash
from flask import render_template, redirect, url_for
from wms.forms.index import LoginForm


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
        if form.userName.data == "admin" and form.passWord.data == 'admin' :
            return redirect(url_for('client.clientList'))
    return render_template('login.html', form = form, pageTitle =pageTitle )


@home_bp.route('/logout')
def logout():
    return render_template('logout.html')
