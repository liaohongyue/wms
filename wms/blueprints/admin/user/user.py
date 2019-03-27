from flask import Blueprint, render_template

user_bp = Blueprint('user',__name__)

@user_bp.route('/userList')
def userList():
    return render_template('admin/user/userList.html')

@user_bp.route('/userInfoEdit')
def userInfoEdit():
    return render_template('admin/user/userInfoEdit.html')

@user_bp.route('/userPasswordEdit')
def userPasswordEdit():
    return render_template('admin/user/userPasswordEdit.html')