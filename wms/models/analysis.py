from wms.extension import db

class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    AnalysisType = db.Column(db.String(20))
    CGroupName = db.Column(db.String(20))
    Csamples = db.Column(db.String(200))
    EGroupName = db.Column(db.String(20))
    Esamples = db.Column(db.String(200))
    remark = db.Column(db.String(200))