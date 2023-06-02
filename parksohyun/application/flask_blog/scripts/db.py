from flask_script import Command
from flask_blog import db
from flask_blog.models.entries import Entry

# (Command)로 설정하는 것으로, 스크립트 실행을 위한 클래스로서 정의된다.
# InitDB는 클래스명
class InitDB(Command):
    # 클래스 설명을 위한 커멘드
    "create database"

    # 실제 스크립트에서 실행되는 내용. db.create_all()을 하는 것으로 모델 정의가 반영
    def run(self):
        db.create_all()