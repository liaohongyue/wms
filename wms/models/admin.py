from wms.extension import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Admin(db.Model, UserMixin):
    __tablename__='admin'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(15))
    gender = db.Column(db.String(5))
    telephone = db.Column(db.String(15))
    email = db.Column(db.String(30))
    unit = db.Column(db.String(30))
    password_hash =db.Column(db.String(200))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
