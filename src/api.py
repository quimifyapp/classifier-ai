import logging
import os
import sys

from flask import Flask, request, after_this_request
from model import Model

app = Flask(__name__)

# Logging:

CONTENT_FORMAT = '%(asctime)s - %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=CONTENT_FORMAT, datefmt=DATE_FORMAT)
logger = logging.getLogger(__name__)


def colored(text, color):
    reset_color = "\033[0m"
    return color + text + reset_color


BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RED = "\033[91m"

UNKNOWN_TAG = colored("Unknown", RED)
INORGANIC_TAG = colored("Inorganic", BLUE)
ORGANIC_TAG = colored("Organic", GREEN)
FORMULA_TAG = colored("Formula", YELLOW)
NAME_TAG = colored("Name", MAGENTA)


# Services:

class Result:
    def __init__(self, response, tag):
        self.response = response
        self.tag = tag


UNKNOWN = Result("", UNKNOWN_TAG + " " * 12)
INORGANIC_FORMULA = Result("inorganicFormula", INORGANIC_TAG + " | " + FORMULA_TAG)
ORGANIC_FORMULA = Result("organicFormula", ORGANIC_TAG + " " * 2 + " | " + FORMULA_TAG)
INORGANIC_NAME = Result("inorganicName", INORGANIC_TAG + " | " + NAME_TAG + " " * 3)
ORGANIC_NAME = Result("organicName", ORGANIC_TAG + " " * 2 + " | " + NAME_TAG + " " * 3)


@app.route("/")
def classify():
    result = UNKNOWN

    input_text = request.args.get('input')
    prediction = formula_name_model.predict(input_text)

    if prediction < 0.5:
        formula_prediction = formula_inorganic_organic_model.predict(input_text)

        if formula_prediction < 0.5:
            result = INORGANIC_FORMULA
        elif formula_prediction > 0.5:
            result = ORGANIC_FORMULA
    elif prediction > 0.5:
        name_prediction = name_inorganic_organic_model.predict(input_text)

        if name_prediction < 0.5:
            result = INORGANIC_NAME
        elif name_prediction > 0.5:
            result = ORGANIC_NAME

    @after_this_request
    def after_request(response):
        Model.cleanup()  # Must be called
        logger.info("{} <- {}".format(result.tag, '"' + input_text + '"'))
        return response

    return result.response


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
