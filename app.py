from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "UTA ID: 1001831207   Name: Sai Parinita Pachalla"
