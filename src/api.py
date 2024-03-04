import logging
import os
import sys

from flask import Flask, request
from model import Model

app = Flask(__name__)

# Constants:

UNKNOWN = ""

INORGANIC_FORMULA = "inorganicFormula"
ORGANIC_FORMULA = "organicFormula"
INORGANIC_NAME = "inorganicName"
ORGANIC_NAME = "organicName"

# Configure logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


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


def with_log(input_text, result):
    label = "unknown" if result == UNKNOWN else result

    red = "\033[91m"
    green = "\033[92m"
    color = red if result == UNKNOWN else green

    logger.info("{:<25} <- {}".format(color + label + "\033[0m", '"' + input_text + '"'))

    return result


@app.route("/")
def classify():
    input_text = request.args.get('input')

    score = formula_name_model.predict(input_text)

    if is_formula(score):
        formula_score = formula_inorganic_organic_model.predict(input_text)

        if is_inorganic_formula(formula_score):
            return with_log(input_text, INORGANIC_FORMULA)
        elif is_organic_formula(formula_score):
            return with_log(input_text, ORGANIC_FORMULA)
    elif is_name(score):
        name_score = name_inorganic_organic_model.predict(input_text)

        if is_inorganic_name(name_score):
            return with_log(input_text, INORGANIC_NAME)
        elif is_organic_name(name_score):
            return with_log(input_text, ORGANIC_NAME)

    return with_log(input_text, UNKNOWN)


# Run at startup:

if __name__ == '__main__':
    if len(sys.argv) < 2:
        logger.error("Usage: python api.py [models directory]")
        sys.exit(1)

    # Check if models directory exists:
    models_directory = sys.argv[1]
    if not os.path.exists(models_directory):
        logger.error("Error: models directory does not exist.")
        sys.exit(1)

    logger.info("Importing models from directory: %s", models_directory)

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
