# 1
from flask import Flask

app = Flask(__name__)
app.config.from_object('salary.config') #(config 파일명

#salary 폴더의 views 폴더의 views파일
import salary.views.views