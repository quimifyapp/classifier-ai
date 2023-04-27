import os
import sys

from flask import Flask
from model import Model

app = Flask(__name__)


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


@app.route('/classify/<text>')
def classify(text):
    return "Will classify " + text + " and return a value in {-1, 0, 1, 2, 3}."


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
    app.run()
