from app import db

# model for data in the database
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    date = db.Column(db.Date)
    description = db.Column(db.String(500))
    complete = db.Column(db.Integer)
