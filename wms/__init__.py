from flask import Flask

from wms.blueprints.home import home_bp
from wms.blueprints.admin.project.clientInfo.client import client_bp
from wms.blueprints.admin.project.analysisInfo.analysis import analysis_bp
from wms.blueprints.admin.project.projectInfo.project import project_bp
from wms.blueprints.admin.project.samplesInfo.samples import samples_bp
from wms.blueprints.admin.user.user import user_bp

from  wms.forms.test import LoginForm

app = Flask('wms')

# config app
app.secret_key='secret key'

# register buleprint
app.register_blueprint(client_bp)
app.register_blueprint(project_bp)
app.register_blueprint(analysis_bp)
app.register_blueprint(home_bp)
app.register_blueprint(samples_bp)
app.register_blueprint(user_bp)