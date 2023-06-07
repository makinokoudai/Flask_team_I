from flask_script import Command
from chat import db
from chat.models.users import User

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()