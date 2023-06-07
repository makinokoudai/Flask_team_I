from flask_script import Command
from gas import db  
from gas.models.gases import Gas

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()