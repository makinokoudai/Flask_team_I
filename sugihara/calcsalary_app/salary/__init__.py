from flask import Flask     #Flask自体をインポート

app = Flask(__name__)       #Flaskのアプリケーション本体を作成

app.config.from_object('salary.config')     #flask_blogにあるconfigファイルをconfigとして扱う

from salary.views import views     #viewsファイルをインポート