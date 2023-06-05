from holiday import app
from flask import request,redirect,url_for,render_template,flash,session

@app.route('/')
def input_entry():
    return render_template('input.html')