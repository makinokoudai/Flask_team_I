from flask_script import Manager
from holiday import app
from holiday.scripts.db import InitDB

# 스크립트 파일을 등록
if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('init_db', InitDB()) # 작성한 InitDB() 모듈을 init_db라는 이름으로 실행할 수 있도록 함
    manager.run()