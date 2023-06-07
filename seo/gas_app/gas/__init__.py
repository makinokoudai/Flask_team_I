from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('gas.config')

db = SQLAlchemy(app)

from gas.views import entries