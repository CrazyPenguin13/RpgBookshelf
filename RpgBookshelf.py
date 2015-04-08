from flask import Flask, render_template, request, redirect, url_for, abort, session
from book_models import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'iG8+9(x^2)'


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
