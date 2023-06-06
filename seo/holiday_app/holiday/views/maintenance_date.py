from holiday import app
from flask import request, redirect, url_for, render_template, flash, session
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route('/new', methods=['POST'])
def add_input():

    if request.form['holiday'] == '':  #空欄のバリデーション
            flash('祝日日付を入力してください')
    else:
        if (request.form['holiday'].isdigit()) and (len(request.form['holiday']) == 8): #8文字の数字意外のバリデーション
            if 'write' in request.form:  #登録・更新ボタンを押したときの処理
                # if request.form['holiday'] == '':
                #     flash('祝日日付を入力してください')
                # else:
                    # if (request.form['holiday'].isdigit()) and (len(request.form['holiday']) == 8):
                        holiday = Holiday.query.filter_by(holi_date=request.form['holiday']).first()  #データベース内の祝日と、入力値の祝日が等しいものを抽出

                        if holiday:  #データベース値と入力値が一致したときの処理
                            holiday.holi_date = request.form['holiday']
                            holiday.holi_text = request.form['holiday_text']
                            db.session.merge(holiday)
                            db.session.commit()
                            flash('{0}は{1}に更新されました'.format(holiday.holi_date, holiday.holi_text))

                        else:  #データベース値と入力値が異なるときの処理
                            holiday = Holiday(
                                holi_date = request.form['holiday'],
                                holi_text = request.form['holiday_text']
                            )
                            db.session.add(holiday)
                            db.session.commit()
                            flash('{0}({1})が登録されました'.format(holiday.holi_date, holiday.holi_text))
                    
                    # else:
                        # flash('祝日日付に8文字の半角数字を入力してください')
                
            elif 'delete' in request.form:  #削除ボタンを押したときの処理
                holiday = Holiday.query.filter_by(holi_date=request.form['holiday']).first()  #データベース内の祝日と、入力値の祝日が等しいものを抽出
                if holiday:  #データベース値と入力値が一致したときの処理
                    holiday = Holiday.query.get(request.form['holiday'])
                    db.session.delete(holiday)
                    db.session.commit()
                    flash('{0}({1})は、削除されました'.format(holiday.holi_date, holiday.holi_text))
                    
                else:  #データベース値と入力値が異なるときの処理
                    flash('{0}は、祝日マスタに登録されていません'.format(request.form['holiday']))

        else:
            flash('祝日日付に8文字の半角数字を入力してください')

    return render_template('result.html')