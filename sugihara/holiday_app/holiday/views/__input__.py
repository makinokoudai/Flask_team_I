from holiday import app
from flask import request,redirect,url_for,render_template,flash,session

@app.route('/')
def input_entry():
    flash('追加の祝日を入力してください')
    return render_template('input.html')


@app.route('/list')
def list_entry():
    flash('一覧を表示しました')
    return render_template('list.html')