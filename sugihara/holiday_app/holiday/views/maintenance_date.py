from flask import request,redirect,url_for,render_template,flash,session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route('/maintenance_date',methods=['POST'])
def add_holiday():
    
    if(request.form['button'] == 'input_date'):
        holi_date = Holiday(
                holiday = request.form['holiday'],
                holiday_text = request.form['holiday_text']
            )
        if(1 == Holiday.query.filter_by(holiday=holi_date.holiday).count()):
            holi_date = Holiday.query.get(request.form['holiday'])
            holi_date.holiday = request.form['holiday']
            holi_date.holiday_text = request.form['holiday_text']
            flash('データを更新しました')
            db.session.merge(holi_date)
            db.session.commit()
        else:     
            flash('データを追加しました')
            db.session.add(holi_date)
            db.session.commit()
        return redirect(url_for('input_entry'))
    
    if(request.form['button'] == 'del_date'):
        if(1 == Holiday.query.filter_by(holiday=request.form['holiday']).count()):
            holi_date = Holiday.query.get(request.form['holiday'])
            db.session.delete(holi_date)
            db.session.commit()
            flash('データを削除しました')
            return redirect(url_for('input_entry'))
        else:
            flash('削除するデータがありませんでした')
    
    if(request.form['button'] == 'list'):
        return redirect(url_for('list_display'))
    
@app.route('/maintenance_date',methods=['GET'])
def list_display():
    list_holiday = Holiday.query.all()
    return render_template('list.html',list_holiday=list_holiday)