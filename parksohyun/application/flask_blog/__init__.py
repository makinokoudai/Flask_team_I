# 1. init.py(어플리케이션 본체 파일)작성
from flask import Flask

# flask의 어플리케이션 본체를 작성
app = Flask(__name__)

# 3) config 파일을 유효화시키기 위해 추가
app.config.from_object('flask_blog.config')

# 지금부터 만드는 views라고 하는 파일을 임포트
import flask_blog.views