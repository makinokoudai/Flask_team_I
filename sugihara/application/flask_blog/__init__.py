from flask import Flask     #Flask自体をインポート
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)       #Flaskのアプリケーション本体を作成

app.config.from_object('flask_blog.config')     #flask_blogにあるconfigファイルをconfigとして扱う

db = SQLAlchemy(app)

from flask_blog.views import views,entries    #viewsファイルをインポート