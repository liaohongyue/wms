from wms.extension import db

class Analysis(db.Model):
    __tablename__='analysis'
    id = db.Column(db.Integer, primary_key=True)
    AnalysisType = db.Column(db.String(20), default = '')
    CGroupName = db.Column(db.String(20), default = '')
    Csamples = db.Column(db.String(200), default = '')
    EGroupName = db.Column(db.String(20), default = '')
    Esamples = db.Column(db.String(200), default = '')
    remark = db.Column(db.String(200), default = '')
    projects_id = db.Column(db.Integer, db.ForeignKey('project.id'))