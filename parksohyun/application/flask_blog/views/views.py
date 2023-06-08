# 2. views.py 작성

# 4) html file을 브라우저에 건넨다
from flask import request, redirect, url_for, render_template, flash, session # 이용할 flask 관련 패키지를 임포트한다
from flask_blog import app
from functools import wraps

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner

# /login이라는 URL에 리퀘스트가 있을 때 루팅 처리
# 메소드를 지정하는 것으로, 그 URL에 대한 HTTP 메소드를 제한하는 것이 가능
# 미지정 시, GET 메소드만 허가된다
# login 링크를 클릭할 땐 GET, 로그인 폼의 데이터 송신 시엔 POST, → 'GET','POST'으로 지정
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('Username is not correct')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('Password is not correct')
        else: # 로그인 성공 시 리다이렉트
            session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    # 그렇지 않으면, 재차 로그인 폼을 표시.
    # GET의 경우, /login을 클릭했을 때는 위의 처리를 통과하지 않으므로, 아래의 로그인 폼을 표시
    return render_template('login.html')

# 로그아웃 시, 홈 화면으로 이동
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))