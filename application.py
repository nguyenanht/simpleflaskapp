from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello world"


if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')
