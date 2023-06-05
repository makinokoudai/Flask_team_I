from flask  import  request, redirect, url_for, render_template, flash, session

from holiday import app
from holiday.models.mst_holiday import Holiday
from holiday import db
from holiday.views.input import validate_text, validate_date

@app.route('/maintenance_date', methods=['POST'])
def crud_holiday():
    holi_date = ""
    holi_text = ""
    crud_kind = ""

    if validate_text(request.form['holi_text']):
         return redirect(url_for('input_holiday'))
    
    if validate_date(request.form['holi_date']):
        return redirect(url_for('input_holiday'))

    is_holiday_exists = Holiday.query.get(request.form['holi_date'])
    crud_kind_button = request.form['button']

    if crud_kind_button == "insert_update":
        holi_date = request.form['holi_date']
        holi_text = request.form['holi_text']

        holi_info = Holiday(
            holi_date=holi_date,
            holi_text=holi_text
        )

        if is_holiday_exists:
            print("update!!!", flush=True)
            crud_kind = "update"
            
            db.session.merge(holi_info)
            db.session.commit()
            
        else:
            print("insert!!!", flush=True)
            crud_kind = "insert"

            db.session.add(holi_info)
            db.session.commit()
            
    if crud_kind_button == "delete":
        if is_holiday_exists:
            crud_kind = "delete"
            holi_date = request.form['holi_date']
            holi_text = is_holiday_exists.holi_text

            db.session.delete(is_holiday_exists)
            db.session.commit()
        else:
            flash(f"{request.form['holi_date']}は、祝日マスタに登録されていません")
            return redirect(url_for('input_holiday'))

        
    return render_template('result.html', holi_date=holi_date, holi_text=holi_text, crud_kind=crud_kind)