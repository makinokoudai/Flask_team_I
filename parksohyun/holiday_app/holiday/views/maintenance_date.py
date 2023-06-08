# 등록, 갱신, 삭제의 데이터 베이스 처리, 그 후 결과 화면 불러들이기
from flask import request, redirect, url_for, render_template, flash, session
from holiday.models.mst_holiday import Holiday
from holiday import app
from holiday import db

@app.route('/maintenance_date', methods=['POST'])
def maint_date():
    
    # html에서 작성한 form
    holiday = request.form['holiday']
    holiday_text = request.form['holiday_text']

    # validation : 공백일 때
    if holiday == '' or holiday_text == '':
        flash('Please fill in the date or text')
        return redirect(url_for('show_home'))
    else:
        selectOne = Holiday.query.get(holiday) # 입력한 holiday(date)라는 객체가 있는지
        whichButton = request.form["button"] # 어느 버튼을 눌렀는지

        # 등록/수정 버튼 눌렀을 때
        if whichButton == "insert_update":
            # 11번째 줄에서 가져온 정보를 새 객체 형태로 나타냄
            new_holiday = Holiday(holiday, holiday_text)
            
            # 등록된 holiday가 있으면 -> 갱신
            if selectOne:

                # 같은 내용(날짜, 텍스트)이 있는지 없는지 확인
                isSame = Holiday.query.filter((Holiday.holi_date == holiday) & (Holiday.holi_text == holiday_text)).first()
                
                # 같은 내용이면 -> 이미 존재하는 휴일입니다. 갱신된 내용은 없습니다.
                if isSame:
                    flash('Holiday already exists. No updates have been made.')
                    return redirect(url_for('show_home'))
                else:    
                    whichButton = 'update'
                    db.session.merge(new_holiday)
                    db.session.commit()
            
            # 등록된 holiday가 없으면 -> 등록
            else:
                whichButton = 'insert'
                db.session.add(new_holiday) # db에 추가
                db.session.commit()

        # 삭제 버튼을 눌렀을 때
        elif whichButton == "delete":
            isDate = Holiday.query.filter_by(holi_date=holiday).first() # DB내 날짜와 입력한 날짜가 일치한 것이 있으면 가져옴
            # alertMsg = None
            # DB에 등록되어있지 않은 날짜일때 -> 홈 화면으로 이동
            if not isDate:
                # alertMsg = "unregistered"
                flash('{}は、祝日マスタに登録されていません'.format(holiday))
                return redirect(url_for('show_home', holiday = holiday))
            # DB에 등록되어 있다면 삭제
            else:
                # alertMsg = "Delete_registered_holiday"
                # 입력한 holiday(date)를 담은 객체 삭제
                db.session.delete(selectOne)
                db.session.commit()
    
    #버튼 누르면 처리 후 output.html을 표시 (출력할 값은 변수에 넣어 같이 저장)
    return render_template('result.html', holiday = holiday, holiday_text = holiday_text, whichButton = whichButton) # 변수 안에 변수를 넣도록