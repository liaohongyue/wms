from flask import Blueprint
from flask import render_template

project_bp = Blueprint('project',__name__)

@project_bp.route('/projectList')
def projectList():
    return render_template('admin/project/projectInfo/projectList.html')

@project_bp.route('/projectAdd')
def projectAdd():
    return render_template('admin/project/projectInfo/projectAdd.html')