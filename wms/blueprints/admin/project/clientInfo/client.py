from flask import Blueprint
from flask import render_template

client_bp = Blueprint('client',__name__)

@client_bp.route('/clientList')
def clientlist():
    return render_template('admin/project/clientInfo/clientList.html')

@client_bp.route('/clientEdit')
def clientEdit():
    return render_template('admin/project/clientInfo/clientEdit.html')