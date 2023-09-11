from flask import Flask, render_template, flash, request
from defines import *

app = Flask(__name__, template_folder="templates")
app.secret_key = "dsddf"


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/translate", methods=["POST", "GET"])
def translate():
    matn = request.form["sentence"]
    matn = Translating(matn)
    flash(matn)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)