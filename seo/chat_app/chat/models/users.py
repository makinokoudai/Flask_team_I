from chat import db
from datetime import datetime
from flask_login import UserMixin, LoginManager

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(120))
    created_at = db.Column(db.DateTime)

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<User id:{} name:{} password:{}>'.format(self.id, self.name, self.password)