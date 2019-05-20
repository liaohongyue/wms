from wms.extension import db

class Project(db.Model):
    __tablename__='project'
    id = db.Column(db.Integer,primary_key=True)
    itemNumber = db.Column(db.String(50))
    samplesDate = db.Column(db.DateTime)
    createLib = db.Column(db.String(10))
    checkoutLib = db.Column(db.String(10))
    isSettle = db.Column(db.String(10))
    amogeneSettle = db.Column(db.String(10))
    novoStage = db.Column(db.String(15))
    novoSettle = db.Column(db.String(10))
    isReleaseData = db.Column(db.String(10))
    period = db.Column(db.String(10))
    downloadInfo = db.Column(db.String(1000))
    remark = db.Column(db.String(200))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    analysis = db.relationship('Analysis', cascade = "all")
    samples = db.relationship('Sample', cascade = "all")
    client = db.relationship('Client', back_populates='projects')