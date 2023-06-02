from flask_blog import db #데이터베이스 모듈을 임포트
from datetime import datetime #투고 일시 등에 사용할 datetime 모듈을 임포트

# 모델에 Entry라는 이름을 붙인다
class Entry(db.Model):
    __tablename__ = 'entries' # 데이터 베이스에 사용될 테이블명
    id = db.Column(db.Integer, primary_key = True) # id라는 속성명을, primary_key로서 정의
    title = db.Column(db.String(50), unique = True) # title은 다른 기사와 중복되지 않을 것 
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    # def __init__()는, 모델이 작성될 때의 표준의 동작을 정의
    def __init__(self, title = None, text = None):
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow()

    # def __repr__(self): 는 없어도 되지만, 실제 모델이 참조될 때의 콘솔에서의 출력 형식을 기재
    def __repr__(self):
        return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)