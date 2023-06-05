from flask  import  request, redirect, url_for, render_template, flash, session

from holiday import app
from holiday.models.mst_holiday import Holiday
from holiday import db

@app.route('/')
def input_holiday():
    return render_template('input.html')

def validate_text(holi_text):
    if holi_text == '':
        flash('祝日の名前を入力してください')
        return True
    elif len(holi_text) > 20:
        flash('祝日の名前は20文字以内で入力してください')
        return True
    return False

def validate_date(holi_date):
    if holi_date == '':
        flash('日付を入力してください')
        return True

    return False