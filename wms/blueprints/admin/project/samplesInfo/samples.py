from flask import Blueprint
from flask import render_template

samples_bp = Blueprint('samples',__name__)

@samples_bp.route('/samplesList')
def samplesList():
    return render_template('admin/project/samplesInfo/samplesList.html')

@samples_bp.route('/samplesAdd')
def samplesAdd():
    return render_template('admin/project/samplesInfo/samplesAdd.html')

@samples_bp.route('/samplesEdit')
def samplesEdit():
    return render_template('admin/project/samplesInfo/samplesEdit.html')