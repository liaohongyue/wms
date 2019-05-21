from wms.extension import db

class Project(db.Model):
    __tablename__='project'
    id = db.Column(db.Integer,primary_key=True)
    itemNumber = db.Column(db.String(50), default = '')
    progress = db.Column(db.String(100),default = '')
    samplesDate = db.Column(db.DateTime)
    createLib = db.Column(db.String(10), default = '')
    checkoutLib = db.Column(db.String(10), default = '')
    isSettle = db.Column(db.String(10), default = '')
    amogeneSettle = db.Column(db.String(10), default = '')
    novoStage = db.Column(db.String(15), default = '')
    novoSettle = db.Column(db.String(10), default = '')
    isReleaseData = db.Column(db.String(10), default = '')
    period = db.Column(db.String(10), default = '')
    downloadInfo = db.Column(db.String(1000), default = '')
    remark = db.Column(db.String(200), default = '')
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    analysis = db.relationship('Analysis', cascade = "all")
    samples = db.relationship('Sample', cascade = "all")
    client = db.relationship('Client', back_populates='projects')
    logs = db.relationship('ProjectLog', cascade = "all")

class ProjectLog(db.Model):
    __tablename__='projectLog'
    id = db.Column(db.Integer, primary_key=True)
    addTime = db.Column(db.DateTime, default = '')
    text = db.Column(db.String(400), default = '')
    progect = db.relationship('Project', back_populates='logs')
    projects_id = db.Column(db.Integer, db.ForeignKey('project.id'))

