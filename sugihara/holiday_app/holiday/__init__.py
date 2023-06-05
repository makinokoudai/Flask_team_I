from flask import Flask

app = Flask(__name__)
app.config.from_object('holiday.config')

from holiday.views import __input__