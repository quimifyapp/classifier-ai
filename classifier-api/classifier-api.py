import sys
from flask import Flask, request

app = Flask(__name__)

# Run at startup:
with open(sys.argv[1], "r") as file:
    static_string = file.read()


@app.route('/foo')
def classifier():
    input_parameter = request.args.get('input')
    return static_string + input_parameter


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python classifier-classifier-api.py [data file path]")
        sys.exit(1)

    app.run("0.0.0.0", port=8000)
