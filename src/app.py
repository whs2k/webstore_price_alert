from flask import Flask

__author__ = 'whs2k'

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def hello_world():
    return "Hello Baby!"

