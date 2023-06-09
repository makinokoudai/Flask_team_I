from todo import db
from datetime import datetime

class Entry(db.Model):
    __tablename__ = 'todolist'

    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text)
    

    def __init__(self, text=None):
        self.text = text

    def __repr__(self):
        return f'<Entory id:{self.id}  text:{self.text}>'