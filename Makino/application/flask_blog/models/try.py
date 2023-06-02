from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLAlchemy_DATABASE_URI'] = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(**{
    "user":os.getenv("DB_USER","root"),
    "password":os.getenv("DB_PASSWORD","mysql"),
    "host":os.getenv("DB_HOST","localhost"),
    "database":os.getenv("DB_DATABESE","ENSHU")
}) 

db = SQLAlchemy(app)

class Hoge(db.Model):
    __tablename__ = "('entries',)"
    
db.reflect()
db.drop_all()
    