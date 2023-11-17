import logging
import os
import sys

from flask import Flask, request
from model import Model

app = Flask(__name__)

# Constants:

EMPTY = ""

INORGANIC_FORMULA = "inorganicFormula"
ORGANIC_FORMULA = "organicFormula"
INORGANIC_NAME = "inorganicName"
ORGANIC_NAME = "organicName"


# Services:

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


def with_log(text, result):
    print("\"" + text + "\"", "->", "\"" + result + "\"")
    return result


@app.route("/")
def classify():
    text = request.args.get('input')

    score = formula_name_model.predict(text)

    if is_formula(score):
        formula_score = formula_inorganic_organic_model.predict(text)

        if is_inorganic_formula(formula_score):
            return with_log(text, INORGANIC_FORMULA)
        elif is_organic_formula(formula_score):
            return with_log(text, ORGANIC_FORMULA)
    elif is_name(score):
        name_score = name_inorganic_organic_model.predict(text)

        if is_inorganic_name(name_score):
            return with_log(text, INORGANIC_NAME)
        elif is_organic_name(name_score):
            return with_log(text, ORGANIC_NAME)

    return with_log(text, EMPTY)


# Run at startup:

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python api.py [models directory]")
        sys.exit(1)

    # Check if models directory exists:
    models_directory = sys.argv[1]
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
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run("0.0.0.0", port=8070)
