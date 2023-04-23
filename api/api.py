#!/usr/bin/python3

import sys
from flask import Flask, request
from predict_class import Predict

app = Flask(__name__)

model = Predict()

@app.route('/s/predict/<example>')
def index(example):
    return str(model.predict(example))

if __name__ == '__main__':
    app.run(debug=True)