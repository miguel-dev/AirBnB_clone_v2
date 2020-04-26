#!/usr/bin/python3
"""Starts a Flask application. List of states"""

from models import storage, State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    values = storage.all(State).values()
    return render_template('7-states_list.html', values=values)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
