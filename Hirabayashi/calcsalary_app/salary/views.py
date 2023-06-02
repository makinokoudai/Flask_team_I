from flask import request, url_for, render_template, flash, redirect,session
from salary import app

@app.route("/", methods=["GET","POST"])
def input():
    return render_template("input.html")


@app.route("/output", methods=["GET","POST"])
def output():
    if request.method == "POST":
        # 未入力の検出
        if request.form["salary"] == "":
            flash("給与が未入力です。入力してください。")
            return redirect(url_for("input"))
        
        # 入力する値がある場合の処理を行う
        salary = int(request.form['salary'])

        # 計算をしない場合の処理を記述
        if salary >= 10000000000:
            flash('給与の最大入力範囲を超えています。')
            session['input_data'] = salary  
            return redirect(url_for("input"))
        elif salary < 0:
            flash('給与は0以上の値を入力して下さい')
            session['input_data'] = salary  
            return redirect(url_for("input"))
        
        # 正常系の処理
        session.pop('input_data', None)  
        if salary > 1000000: 
            tax_amount = int((salary - 1000000) * 0.2 + (1000000 * 0.1))
        else:
            tax_amount = int(salary * 0.1)
        pay_amount = salary - tax_amount
        salary = "{:,}".format(salary)
        tax_amount = "{:,}".format(tax_amount)
        pay_amount = "{:,}".format(pay_amount)
        flash("計算に成功しました。")
        
    return render_template("output.html", salary=salary, pay_amount=pay_amount, tax_amount=tax_amount)
