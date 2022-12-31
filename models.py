from sqlalchemy import true
from . import db
from flask_login import UserMixin #custom class, gives user specific things for login
from sqlalchemy.sql import func #gets current date and time

#Notes class
class Note(db.Model):
    id = db.Column(db.Integer, primary_key = true)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


#user class
class User(db.Model, UserMixin):

    #defining all fields in database for every user object
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')  



