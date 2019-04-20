from wms.extension import db

class Project(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    itemNumber = db.Column(db.String(50))
    remark = db.Column(db.String(200))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    analysis = db.relationship('Analysis')
    samples = db.relationship('Sample')