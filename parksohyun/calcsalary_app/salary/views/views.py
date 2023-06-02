# 2
from flask import request, redirect, url_for, render_template, flash, session
from salary import app

# @app.route('/')
# def show_views():
#     return render_template('layout.html') # 루트가 '/'일 때 layout.html을 표시

@app.route('/')
def show_input():
    return render_template("input.html")

@app.route('/output', methods=['GET','POST'])
def show_output():
    if request.method == 'POST':
        salary = int(request.form['salary']) # number와 관계 없음
        if salary <= 1000000:
            tax = 0.1
            tax_money = salary * tax    
        else:
            tax = 0.2
            tax_money = (salary - 1000000) * tax + (1000000 * 0.1)
        money = salary - tax_money
    return render_template('output.html', sal=salary, mon = money, tax = tax_money) # 변수 안에 변수를 넣도록
