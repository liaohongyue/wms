from wms.extension import db

class Client(db.Model):
    __tablename__='client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    organization = db.Column(db.String(25))
    gender = db.Column(db.String(5))
    email = db.Column(db.String(100))
    telephone = db.Column(db.String(15))
    address = db.Column(db.String(100))
    remark = db.Column(db.String(500))
    projects = db.relationship('Project')