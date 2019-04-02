from wms.extension import db

class Sample(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    amogeneItem = db.Column(db.String(30))
    species = db.Column(db.String(30))
    libraryType = db.Column(db.String(30))
    seqType = db.Column(db.String(50))
    indexItem = db.Column(db.String(30))
    indexForward = db.Column(db.String(30))
    extractStatus = db.Column(db.String(20))
    seqTimes = db.Column(db.String(20))
    seqDose = db.Column(db.String(20))
    sampleType = db.Column(db.String(30))
    charName = db.Column(db.String(30))
    remark = db.Column(db.String(200))