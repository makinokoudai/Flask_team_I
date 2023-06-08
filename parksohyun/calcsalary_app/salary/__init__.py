# 1
from flask import Flask

app = Flask(__name__) # flask 앱 본체 작성
app.config.from_object('salary.config') # config 파일명

# salary 폴더 아래 views 폴더 아래 views파일
import salary.views.views