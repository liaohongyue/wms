from wms.extension import db

class Project(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    itemNumber = db.Column(db.String(50))
    remark = db.Column(db.String(200))