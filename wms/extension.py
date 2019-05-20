from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    from wms.models.admin import Admin
    user = Admin.query.get(int(user_id))
    return user

login_manager.login_view = 'index.login'
login_manager.login_message_category = '请先登录'


