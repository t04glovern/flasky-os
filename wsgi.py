from flask import Flask, jsonify
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/api/v2/test")
def test():
    return jsonify("{\"hello\": \"World!\"}")

if __name__ == "__main__":
    application.run()
