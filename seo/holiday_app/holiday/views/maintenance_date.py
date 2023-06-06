from holiday import app
from flask import request, redirect, url_for, render_template, flash, session
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route('/new', methods=['POST'])
def add_input():
    # if Holiday.query.get()
    if 'write' in request.form:
        holiday = Holiday(
            holi_date = request.form['holiday'],
            holi_text = request.form['holiday_text']
        )
        db.session.add(holiday)
        db.session.commit()
        flash('祝日が追加されました')
        
    elif 'delete' in request.form:
        holiday = Holiday.query.get(request.form['holiday'])
        db.session.delete(holiday)
        db.session.commit()
        flash('祝日が削除されました')
        return redirect(url_for('show_input'))


    return render_template('result.html')