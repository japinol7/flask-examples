from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Flask 02 Example. Calling APIs')


@app.route('/about')
def about():
    return render_template('about.html')
