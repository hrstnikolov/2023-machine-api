from flask import Flask

app = Flask(__name__)


@app.route('/')
def landing_page():
    return 'Welcome to Machine API!'


if __name__ == '__main__':
    app.run()
