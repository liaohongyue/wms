from wms.extension import db

class Sample(db.Model):
    __tablename__='sample'
    id = db.Column(db.Integer, primary_key = True)
    amogeneItem = db.Column(db.String(30), default = '')
    species = db.Column(db.String(30), default = '')
    libraryType = db.Column(db.String(30), default = '')
    seqType = db.Column(db.String(50), default = '')
    indexItem = db.Column(db.String(30), default = '')
    indexForward = db.Column(db.String(30), default = '')
    extractStatus = db.Column(db.String(20), default = '')
    seqTimes = db.Column(db.String(20), default = '')
    seqDose = db.Column(db.String(20), default = '')
    sampleType = db.Column(db.String(30), default = '')
    chartName = db.Column(db.String(30), default = '')
    remark = db.Column(db.String(200), default = '')
    projects_id = db.Column(db.Integer, db.ForeignKey('project.id'))