from holiday import db
from datetime import datetime

# 클래스에 의한 모델 정의
class Holiday(db.Model):
    __tablename__ = 'holiday'
    # 속성 정의
    holi_date = db.Column(db.Date, primary_key=True)
    holi_text = db.Column(db.VARCHAR(20))

    # 모델이 작성되었을 때의 처리를 정의
    def __init__(self, holi_date=None, holi_text=None):
        self.holi_date = holi_date
        self.holi_text = holi_text

    # 참조되었을 때의 표시 포맷 정의
    def __repr__(self):
        return '<Entry date:{} text:{}>'.format(self.holi_date, self.holi_text)