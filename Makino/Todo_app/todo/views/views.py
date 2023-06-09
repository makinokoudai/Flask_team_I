from flask  import  request, redirect, url_for, render_template, flash, session
from todo import app
from todo import db
from todo.models.entries import Entry
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
def show_main():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register_text():
    
    entry = Entry(
        text = request.form.get('text')
    )
    
    db.session.add(entry)
    db.session.commit()
    
    #データを取得して、index.htmlに値を渡す
    get_text_li = Entry.query.all()

    
    return render_template('index.html',get_text_li=get_text_li)

@app.route('/delete/<int:id>',methods=['GET'])
def delete(id):
    print(id)
    Entry.query.filter(Entry.id== id).delete()
    
    db.session.commit()
    
    
    #データを取得して、index.htmlに値を渡す
    get_text_li = Entry.query.all()
    return render_template('index.html',get_text_li=get_text_li)
    

    
    
    
    