from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()  

class Players(db.Model,UserMixin):
    __tablename__ = "players"
    player_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    dob = db.Column(db.DateTime)
    role = db.Column(db.String(64))
    last_login = db.Column(db.DateTime)
    username = db.Column(db.String(64))
    password = db.Column(db.String(255))
    screenName = db.Column(db.String(100))
    phone = db.Column(db.String(64))
    phone_type = db.Column(db.String(50))
    

    def __init__(self,first_name, last_name, username, password, dob, phone,phone_type,fav_game):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_type = phone_type
        self.username = username
        self.password = password
        self.dob = dob
        self.phone = phone
        self.fav_game = fav_game

    def is_authenticated(self):
        return True