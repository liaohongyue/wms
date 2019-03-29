from flask_sqlalchemy import SQLAlchemy
db  = SQLAlchemy()

class Admin(db.Model):
    id = db.Column(db.Integer, autoincrement, primary_key= True)
    gender = db.Column(db.String(5))
    telephone = db.Column(db.String(15))
    email = db.Column(db.String(30))
    unit = db.Column(db.String(30))
    password_hash = (db.String(200))
