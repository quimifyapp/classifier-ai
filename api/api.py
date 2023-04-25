#!/usr/bin/python3

from flask import Flask
from model import Model

app = Flask(__name__)

model = Model()


@app.route('/formula-name/<text>')
def formula_or_name(text):
    return str(model.predict(text))


if __name__ == '__main__':
    app.run(debug=True)  # TODO disable
