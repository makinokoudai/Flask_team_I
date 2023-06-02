from salary import app      #appをインポート
from flask import request,redirect,url_for,render_template,flash,session    #Flaskのパッケージをインポート

salary = 0
tax = 0
pay_amount = 0

@app.route('/')     #urlにリクエストがあった際に以下の処理を実行
def input_salary():
    return render_template('input.html')

@app.route('/output', methods=['POST'])     #urlにリクエストがあった際に以下の処理を実行
def output_salary():
     if request.method == 'POST':
        salary = int(request.form['salary'])
        if salary > 1000000:
            tax = int(0.2*(salary-1000000) + 10000)
            pay_amount = salary - tax
        return render_template('output.html',salary_d=salary,tax_d=tax,pay_amount_d=pay_amount)
     else:
         return render_template('input.html')

