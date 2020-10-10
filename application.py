from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def indexmain():
    return render_template("index.html")


@app.route("/<string:name>")
def index(name):
    return render_template('index.html', name = name.capitalize())