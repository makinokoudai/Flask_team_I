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
    
    text_len = len(entry.holi_text)
    
    get_btn_val = request.form.get('button')
    
    # if get_btn_val ==  "delete": #消去ボタンかの判断処理
    #     if exists_data:
    #         # db.session.delete(entry)
    #         rtn_text = f"{entry.holi_date}({entry.holi_text})が削除されました。"
    #         Entry.query.filter(Entry.holi_date==entry.holi_date).delete()
    #     else:
    #         rtn_text = "データが存在しません。"
        
    
    # else :
        
    exists_data = Entry.query.filter(Entry.holi_date == entry.holi_date).first()
    
    if text_len <= 20:  #受け取った文字が20文字以内か調べる
        if entry.holi_date != "" and  entry.holi_text !="": #受け取った値がNullかを調べる
            
        
            # get_text = Entry.query.filter(Entry.holi_date == entry.holi_date) 
                

            rtn_text =""
            
            if text_len <= 20:
                if get_btn_val == "insert_update":
                    if exists_data:
                        exists_data.holi_date = entry.holi_date
                        exists_data.holi_text = entry.holi_text
                        rtn_text = f"{entry.holi_date}({entry.holi_text})が更新されました。"
                    else:
                        db.session.add(entry)
                        rtn_text = f"{entry.holi_date}({entry.holi_text})が登録されました。"
                    # rtn_message_page = "register_page"  
            
            else:
                
                flash('テキストは20文字以内で入力してください。')
                return redirect(url_for('show_input'))
                
                
        elif entry.holi_date != "":
            if get_btn_val == "delete":
                if exists_data:
                    # db.session.delete(entry)
                    rtn_text = f"{entry.holi_date}({entry.holi_text})が削除されました。"
                    Entry.query.filter(Entry.holi_date==entry.holi_date).delete()
                else:
                    rtn_text = "データが存在しません。"

            db.session.commit()
            
            
            return render_template('result.html',text=rtn_text)   
            
        else :
            flash('データが空です。データを入力してください。')
            return redirect(url_for('show_input'))
        
    
    else:
        flash('テキストは20文字以内で入力してください。')
        return redirect(url_for('show_input'))
        
        
    

        

        
    



@app.route('/list')
def display_list():
    
    holidays = Entry.query.all()
    
    return render_template('list.html',holidays=holidays)
    





    
