#!/usr/bin/python3
""" script that star a flask wapp """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ index route """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ /hbnb route  """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """ /c/<text> route, w arg """
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
