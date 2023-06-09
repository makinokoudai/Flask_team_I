from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('todo.config')

app.secret_key = 'user'

db = SQLAlchemy(app)

from todo.views import views