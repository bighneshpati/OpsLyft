from flask import Flask


app = Flask(__name__)


@app.route("/")
def helloWorld():
    return "Hello World ! This is my deployment"

if __name__ == "__main__":
    app.run(host="0.0.0.0")