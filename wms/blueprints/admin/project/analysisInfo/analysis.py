from flask import Blueprint
from flask import render_template

analysis_bp = Blueprint('analysis',__name__)

@analysis_bp.route('/analysisList')
def analysisList():
    return render_template('admin/project/analysisInfo/analysisList.html')

@analysis_bp.route('/analysisEdit')
def analysisEdit():
    return render_template('admin/project/analysisInfo/analysisEdit.html')