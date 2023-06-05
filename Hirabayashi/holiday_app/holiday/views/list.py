from flask  import  request, redirect, url_for, render_template, flash, session

from holiday import app
from holiday.models.mst_holiday import Holiday
from holiday import db

@app.route('/list')
def display_holidays():
    holidays = Holiday.query.all()
    return render_template('list.html', holidays = holidays)