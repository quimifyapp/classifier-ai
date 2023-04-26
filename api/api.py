#!/usr/bin/python3

from flask import Flask
from model import Model

app = Flask(__name__)

model = Model()


@app.route('/formula-or-name/<text>')
def formula_or_name(text):
    return str(model.formula_or_name(text))


@app.route('/formula-inorganic-or-organic/<text>')
def formula_inorganic_or_organic(text):
    return str(model.formula_inorganic_or_organic(text))


@app.route('/name-inorganic-or-organic/<text>')
def name_inorganic_or_organic(text):
    return str(model.name_inorganic_or_organic(text))


@app.route('/classify/<text>')
def classify(text):
    return str(model.classify(text))


if __name__ == '__main__':
    app.run(debug=True)  # TODO disable
