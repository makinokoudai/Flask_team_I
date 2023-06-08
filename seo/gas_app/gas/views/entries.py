from flask import render_template, redirect, flash, url_for, request, session
from gas import app, db
from gas.models.gases import Gas    


def check_int(num):
    if isinstance(num, int) == False:
        flash('整数を入力してください')
        return redirect(url_for('show_nenpi'))
    else:
        if num < 0:
            flash('正の整数を入力してください')
            return redirect(url_for('show_nenpi'))
        
def check_brunk(num):
    if num == '':
        flash('値を入力してください')
        redirect(url_for('show_nenpi'))
    

@app.route('/')
def show_entries():
    gases = Gas.query.order_by(Gas.created_at.desc()).all()
    return render_template('index.html', gases=gases)

@app.route('/search', methods=['POST'])
def search_nenpi():
    content = request.form.get('search')
    gases = Gas.query.filter_by(car=content).all()
    flash('検索結果')
    print(content)
    return render_template('index.html', gases=gases)

@app.route('/nenpi_calc')
def show_nenpi():
    return render_template('nenpi_calc.html')

@app.route('/nenpi_calc/result', methods=['POST'])
def result_nenpi():
    if request.method == 'POST':
        if request.form['start'] != '' and request.form['goal'] != '' and request.form['price'] != '' and request.form['gas'] != '':
            long = int(request.form.get('goal')) - int(request.form.get('start'))
            gas_l = int(request.form.get('gas'))
            price = int(request.form.get('price'))

            nenpi = round(long / gas_l, 1)
            total_price = round(price * gas_l, 0)
            return render_template('nenpi_calc_result.html', nenpi=nenpi, price=total_price)
        else:
            flash('値を入力してください')
            return redirect(url_for('show_nenpi'))
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
    
@app.route('/nenpi_edit/<int:id>/edit', methods=['GET'])
def show_edit(id):
    gas = Gas.query.get(id)
    return render_template('nenpi_edit.html', gas=gas)

@app.route('/nenpi_edit/<int:id>', methods=['POST'])
def update_nenpi(id):
    gas = Gas.query.get(id)
    gas.car = request.form.get('car')
    gas.extra = request.form.get('extra')
    db.session.merge(gas)
    db.session.commit()
    flash('記録を編集しました')
    return redirect(url_for('show_entries'))

@app.route('/<int:id>', methods=['POST'])
def delete_nenpi(id):
    gas = Gas.query.get(id)
    db.session.delete(gas)
    db.session.commit()
    flash('記録が削除されました')
    return redirect(url_for('show_entries'))
