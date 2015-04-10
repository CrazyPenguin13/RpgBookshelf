from flask import Flask, render_template, request, redirect, url_for, abort, session
from flask_bootstrap import Bootstrap
from data_models import *

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'iG8+9(x^2)'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['BOOTSTRAP_USE_MINIFIED'] = False
Bootstrap(app)


@app.route('/')
def home():
    bookList = []  # Book.query.limit(30).all()
    return render_template('index.html', books=bookList)


@app.route('/about')
def about():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/search')
def search():
    return render_template('search.html')


if __name__ == '__main__':
    db.init_app(app)
    app.run()

