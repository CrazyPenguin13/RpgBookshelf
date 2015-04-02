from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Nothing here yet... but someday!'


if __name__ == '__main__':
    app.run()
