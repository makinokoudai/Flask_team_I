from holiday import app
from flask import request, redirect, url_for, render_template, flash, session
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route('/new', methods=['POST'])
def add_input():
    holiday = Holiday(
        holi_date = request.form['holiday'],
        holi_text = request.form['holiday_text']
    )
    db.session.add(holiday)
    db.session.commit()
    flash('祝日が追加されました')

    return render_template(url_for('result.html'))