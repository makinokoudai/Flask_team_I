from flask_blog import app      #appをインポート
from flask import request,redirect,url_for,render_template,flash,session    #Flaskのパッケージをインポート

@app.route('/')     #urlにリクエストがあった際に以下の処理を実行
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session['logged_in']=True
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))