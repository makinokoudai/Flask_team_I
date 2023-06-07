from holiday import app
from flask import request, redirect, url_for, render_template, flash, session

@app.route('/')
def show_input():
    return render_template('input.html')