# 2. views.py 작성

# 4) html file을 브라우저에 건넨다
from flask import request, redirect, url_for, render_template, flash, session # 이용할 flask 관련 패키지를 임포트한다
from flask_blog import app

# URL에 액세스가 있었을 때만 
@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect('/login')
    # 5) templates 폴더 이하에 있는 entries/index.html를 반환해 렌더링해 준다
    # 경로에 templates를 지정하지 않은 이유는, 
    # templates 폴더 이하에 자동으로 html파일이 있는 것을 인식해 주기 때문
    # flask에서는, html파일은 templates 폴더아래 작성된다는 룰로 되어있다고 기억할 것
    return render_template('entries/index.html')

# 이 파일에서는, http://127.0.0.1:5000/에 리퀘스트가 있었을 때 처리

# /login이라는 URL에 리퀘스트가 있을 때 루팅 처리
# 메소드를 지정하는 것으로, 그 URL에 대한 HTTP 메소드를 제한하는 것이 가능
# 미지정 시, GET 메소드만 허가된다
# 이번에는, login 링크를 클릭할 땐 GET, 
# 로그인 폼의 데이터 송신 시엔 POST메소드가 사용되므로, 
# 'GET','POST'으로 지정
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            print('Username is not correct')
        elif request.form['password'] != app.config['PASSWORD']:
            print('Password is not correct')
        else:
            session['logged_in'] = True
            # 올바를 때는, /로 리다이렉트시키고, 
            return redirect('/')
    # 그렇지 않으면 render_template('login.html')만이 실행
    # GET의 경우, /login을 클릭했을 때는 이 처리를 통과하지 않으므로
    # render=template('login.html')만이 실행되어, 로그인 폼이 표시됨
    return render_template('login.html')

# 로그아웃 되었을 때 표시. 홈 화면으로 이동
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')