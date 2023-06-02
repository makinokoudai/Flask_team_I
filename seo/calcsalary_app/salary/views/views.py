from flask import request, redirect, url_for, render_template, flash, session
from salary import app

@app.route('/')
def entries():
    return render_template('entries/index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        salary = int(request.form['salary'])
        if str(salary) == '':
            flash("値が未入力です。入力してください。")
            return redirect(url_for('entries'))
        elif salary < 0:
            flash("給与にはマイナスの値は入力できません。")
            return redirect(url_for('entries'))
        elif len(str(salary)) > 10:
            flash("給与には最大9,999,999,999まで入力可能です。")
            return redirect(url_for('entries'))
        else:
            if salary > 1000000:
                over_100 = salary - 1000000
                upper_tax = over_100 * 0.2
                lower_tax = 1000000 * 0.1
                tax = upper_tax + lower_tax
            else:
                tax = salary * 0.1
        
            supply = salary - tax
            return render_template('result.html', salary_display=salary, supply_display=supply, tax_display=tax)