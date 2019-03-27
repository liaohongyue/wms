from flask import Blueprint
from flask import render_template, redirect, url_for

home_bp = Blueprint('index',__name__)

@home_bp.route('/')
def index():
    print(url_for('index.login'))
    return redirect(url_for('index.login'))

@home_bp.route('/test')
def test():
    return render_template('base/projectBase.html')

@home_bp.route('/login')
def login():
    return render_template('login.html')

@home_bp.route('/logout')
def logout():
    return render_template('logout.html')
