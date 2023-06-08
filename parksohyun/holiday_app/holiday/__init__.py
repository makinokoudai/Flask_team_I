# 1
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # flask 앱 본체 작성
app.config.from_object('holiday.config') # config 파일명

db = SQLAlchemy(app)

# salary 폴더 아래 views 폴더 아래 임포트할 파일명 불러들이기
from holiday.views import input, list, maintenance_date