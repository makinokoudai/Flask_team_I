from flask  import  request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday.models.mst_holiday import Entry
from holiday import db
import os


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)



@app.route('/')
def show_input():
    return render_template('input.html')

# データの新規登録と更新処理
@app.route('/entries', methods=['POST'])
def new_entry():
    entry = Entry(
        holi_date = request.form.get('holiday'),
        holi_text = request.form.get('holiday_text')
    )
    
    #受け取った値がNullかを調べる
    if entry.holi_date != "" and  entry.holi_text !="":
        print("データあります new")
        exists_data = Entry.query.filter(Entry.holi_date == entry.holi_date).first()
    
        get_text = Entry.query.filter(Entry.holi_date == entry.holi_date) 
            
        print(get_text)
            
        get_btn_val = request.form.get('button')
            
            
        rtn_text =""
            
        if get_btn_val == "insert_update":
            if exists_data:
                exists_data.holi_date = entry.holi_date
                exists_data.holi_text = entry.holi_text
                rtn_text = f"{entry.holi_date}({entry.holi_text})が更新されました。"
            else:
                db.session.add(entry)
                rtn_text = f"{entry.holi_date}({entry.holi_text})が登録されました。"
            # rtn_message_page = "register_page"    
        elif get_btn_val == "delete":
            if exists_data:
                # db.session.delete(entry)
                rtn_text = f"{entry.holi_date}({entry.holi_text})が削除されました。"
                Entry.query.filter(Entry.holi_date==entry.holi_date).delete()
                
            else:
                rtn_text = "データが存在しません。"
            # rtn_message_page = "delete_data" 
                

            
        db.session.commit()
        
        
        return render_template('result.html',text=rtn_text)   
        
    else :
        # print("データがないです")
        flash('データが空です。データを入力してください。')
        return redirect(url_for('show_input'))
        

        
    



@app.route('/list')
def display_list():
    
    holidays = Entry.query.all()
    
    return render_template('list.html',holidays=holidays)
    





    
