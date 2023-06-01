from flask import Flask     #Flask自体をインポート

app = Flask(__name__)       #Flaskのアプリケーション本体を作成

app.config.from_object('flask_blog.config')     #flask_blogにあるconfigファイルをconfigとして扱う

import flask_blog.views     #viewsファイルをインポート