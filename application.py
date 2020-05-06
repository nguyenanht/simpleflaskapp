from flask import Flask, jsonify

application = Flask(__name__)


@application.route("/")
def index():
    return jsonify({"hello": "world", "from": "index"})


@application.route("/foo")
def foo():
    return jsonify({"hello": "world", "from": "foo"})


if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')
