import os
import sys

from flask import Flask
from model import Model

app = Flask(__name__)

# Services:

NOT_FOUND_RESULT_CODE = "-1"
INORGANIC_FORMULA_RESULT_CODE = "0"
ORGANIC_FORMULA_RESULT_CODE = "1"
INORGANIC_NAME_RESULT_CODE = "2"
ORGANIC_NAME_RESULT_CODE = "3"


def is_formula(score):
    return score < 0.5


def is_name(score):
    return score > 0.5


def is_inorganic_formula(score):
    return score < 0.5


def is_organic_formula(score):
    return score > 0.5


def is_inorganic_name(score):
    return score < 0.5


def is_organic_name(score):
    return score > 0.5


@app.route('/classify/<text>')
def classify(text):
    score = formula_name_model.predict(text)

    if is_formula(score):
        score = formula_inorganic_organic_model.predict(text)

        if is_inorganic_formula(score):
            return INORGANIC_FORMULA_RESULT_CODE
        elif is_organic_formula(score):
            return ORGANIC_FORMULA_RESULT_CODE
    elif is_name(score):
        score = name_inorganic_organic_model.predict(text)

        if is_inorganic_name(score):
            return INORGANIC_NAME_RESULT_CODE
        elif is_organic_name(score):
            return ORGANIC_NAME_RESULT_CODE

    return NOT_FOUND_RESULT_CODE


# Test methods: TODO REMOVE

@app.route('/formula-or-name/<text>')  # Testing
def formula_or_name(text):
    prediction = formula_name_model.predict(text)
    return '{:.10f}'.format(prediction)


@app.route('/formula-inorganic-or-organic/<text>')  # Testing
def formula_inorganic_or_organic(text):
    prediction = formula_inorganic_organic_model.predict(text)
    return '{:.10f}'.format(prediction)


@app.route('/name-inorganic-or-organic/<text>')  # Testing
def name_inorganic_or_organic(text):
    prediction = name_inorganic_organic_model.predict(text)
    return '{:.10f}'.format(prediction)


# Run at startup:

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python api.py [models directory]")
        sys.exit(1)

    # Check if models directory exists:
    models_directory = sys.argv[1]  # "..", "builder", "models"
    if not os.path.exists(models_directory):
        print("Error: models directory does not exist.")
        exit()

    print("Importing models from directory:", models_directory)

    # Locate models:
    formula_name_path = os.path.join(models_directory, "formula-name-model")
    formula_inorganic_organic_path = os.path.join(models_directory, "formula-inorganic-organic-model")
    name_inorganic_organic_path = os.path.join(models_directory, "name-inorganic-organic-model")

    # Load models:
    formula_name_model = Model(formula_name_path)
    formula_inorganic_organic_model = Model(formula_inorganic_organic_path)
    name_inorganic_organic_model = Model(name_inorganic_organic_path)

    # Run Flask app:
    app.run("0.0.0.0", port=8070)
