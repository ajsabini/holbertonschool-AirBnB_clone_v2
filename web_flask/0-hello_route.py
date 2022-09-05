#!/usr/bin/python3
""" script that star a flask wapp """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ hello hbnb in browser """
    return 'Hello HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
