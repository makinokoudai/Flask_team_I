from flask import render_template, redirect, flash, url_for, request, session
from gas import app, db
from gas.models.gases import Gas

@app.route('/')
def show_entries():
    gases = Gas.query.order_by(Gas.created_at.desc()).all()
    return render_template('index.html', gases=gases)

@app.route('/nenpi_calc')
def show_nenpi():
    return render_template('nenpi_calc.html')

@app.route('/nenpi_calc/result', methods=['POST'])
def result_nenpi():
    if request.method == 'POST':
        long = int(request.form.get('goal')) - int(request.form.get('start'))
        gas_l = int(request.form.get('gas'))
        price = int(request.form.get('price'))

        nenpi = round(long / gas_l, 1)
        total_price = round(price * gas_l, 0)
        return render_template('nenpi_calc_result.html', nenpi=nenpi, price=total_price)
    else:
        flash('計算に失敗しました')
        return redirect(url_for('show_nenpi'))  #登録失敗後に前の画面に戻るには？
    
@app.route('/nenpi_write/<float:nenpi>/<int:price>/new', methods=['GET'])
def write_nenpi(nenpi, price):
    return render_template('nenpi_write.html', nenpi=nenpi, price=price)

@app.route('/nenpi_write', methods=['POST'])
def add_nenpi():
    if request.method == 'POST':
        gas = Gas(
            car = request.form['car'],
            nenpi = request.form['nenpi'],
            price = request.form['price'],
            extra = request.form['extra']
        )
        db.session.add(gas)
        db.session.commit()
        flash('新しく記録されました')
        return redirect(url_for('show_entries'))
    else:
        flash('記録に失敗しました')
        return redirect(url_for('show_entries'))