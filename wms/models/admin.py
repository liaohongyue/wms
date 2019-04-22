from wms.extension import db

class Admin(db.Model):
    __tablename__='admin'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(15))
    gender = db.Column(db.String(5))
    telephone = db.Column(db.String(15))
    email = db.Column(db.String(30))
    unit = db.Column(db.String(30))
    password_hash = (db.String(200))
