from salary import app
from flask import render_template,request,redirect,url_for,flash,session
from salary.calc.calcsalary import calc_salary

@app.route('/')
def show_main():
    return render_template('input.html') 



@app.route('/output',methods=['POST'])
def show_output():
    if request.method == 'POST':
        number = request.form.get('number1')
        if number:
            if len(number) > 10:
                flash("給与には最大9,999,999,999まで入力可能です。")
                return render_template("input.html")
            elif int(number) < 0:
                flash("給与にはマイナスの値は入力できません。")
                return render_template("input.html")
            else:
                get_text = calc_salary(int(number))
                return render_template("output.html",x=get_text)
                
        else:
            flash('給料が未入力です。入力してください。')
            return render_template("input.html")
            # return "失敗しました。"
