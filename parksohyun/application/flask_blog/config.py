# 4. config.py 작성 
SQLALCHEMY_DATABASE_URI = 'sqlite:///flask_blog.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True # 1) DEBUG를 ON으로 한다는 뜻 → server.py의 debug=True는 삭제 처리
#
SECRET_KEY = 'secret key'
# 
USERNAME = 'john'
PASSWORD = 'due123'

import os

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(**{
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "mysql"),
    "host": os.getenv("DB_HOST", "localhost"),
    "database": os.getenv("DB_DATABASE", "ENSHU")
})

SQLALCHEMY_TRACK_MODIFICATIONS = False