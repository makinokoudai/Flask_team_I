from flask import request, redirect, url_for, render_template, flash, session
from chat import app
from chat import db
from chat.models.users import User
from wtforms import StringField, PasswordField, Form
from wtforms.validators import InputRequired, Length
from flask_login import UserMixin, LoginManager

# class SignupForm(Form):
#     name = StringField('Name', validators=[InputRequired(), Length(min=4, max=50)])
#     password = PasswordField('Password',  validators=[InputRequired(), Length(min=4, max=120)])

@app.route('/')
def show_entries():
    return render_template('index.html')

@app.route('/result/new', methods=['GET','POST'])
def show_signup():
    return render_template('signup.html')

@app.route('/result', methods=['POST'])
def signup():
    # form = SignupForm(request.form)
    if request.method == 'post':
        user = User(
            name = request.form['name'],
            password = request.form['password']
        )
        db.session.add(user)
        db.session.commit()
        flash('ユーザー登録が完了しました')
        return redirect(url_for('show_entries'))
    else:
        flash('登録に失敗しました')
        return redirect(url_for('show_signup'))
