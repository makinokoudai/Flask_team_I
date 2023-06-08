from flask_script import Command # flask-script 라이브러리 임포트
from holiday import db 

class InitDB(Command):
    "create database" # 클래스 설명을 위한 코멘트

    def run(self): # 실제 스크립트에서 실행되는 내용
        db.create_all() # 모델 정의 반영