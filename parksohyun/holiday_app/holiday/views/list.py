# # 일람 화면 불러들이기

from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday.models.mst_holiday import Holiday
from holiday import db

@app.route('/list')
def show_allList():
    allHolidays = Holiday.query.all()
    return render_template('list.html', allHolidays = allHolidays)