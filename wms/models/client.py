from wms.extension import db

class Client(db.Model):
    __tablename__='client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    organization = db.Column(db.String(25), default = '')
    gender = db.Column(db.String(5))
    email = db.Column(db.String(100), default = '')
    telephone = db.Column(db.String(15), default = '')
    address = db.Column(db.String(100), default = '')
    remark = db.Column(db.String(500), default = '')
    projects = db.relationship('Project', back_populates='client', cascade = "all")