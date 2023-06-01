# hello.py

from flask import Flask

# flask 인스턴스 생성
app = Flask(__name__)

# 웹 표현: route()메소드 사용
# 맨 앞에 @가 붙는 것은 장식자(decorator)를 나타낸다
# flask에서는 이러한 장식자가 URL 연결에 활용된다
# 장식자를 사용하면 다음 행의 함수부터 장식자가 적용된다
@app.route('/')

# 함수 실행 시 결과 리턴
def hello_world():
    return "Hello World"

if __name__=='__main__':
    # 웹 앱 실행 요청
    app.run()
