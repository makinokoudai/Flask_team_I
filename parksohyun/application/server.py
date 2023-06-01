# 3. 기동 파일 server.py 작성
from flask_blog import app

if __name__ == '__main__':
    # app.run(debug=True) # 2) config.py 설정 후 app.run()로 변경
    app.run()