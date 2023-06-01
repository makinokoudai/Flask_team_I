from flask_blog import app

@app.route('/')
def show_entries():
    return "Hello World!"

@app.route('/conban')
def show_entries1():
    return "Conban World!"