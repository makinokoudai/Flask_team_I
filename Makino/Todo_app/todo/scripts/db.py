from flask_script import Command
from todo import db
from todo.models.entries import Entry

class InitDB(Command):
    "create database"
    def run(self):
        db.create_all()