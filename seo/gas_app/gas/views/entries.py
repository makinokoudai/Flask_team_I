from flask import render_template, redirect, flash, url_for, request, session
from gas import app, db

@app.route('/')
def show_entries():
    return render_template('index.html')