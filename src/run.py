from src.app import app

__author__ = 'whs2k'

app.run(debug=app.config['DEBUG'], port=4990)