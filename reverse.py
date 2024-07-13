from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Enter your name in the URL :)"

@app.route("/<name>")
def reverse(name):
    return "<h4>{}</h4>".format(name[::-1])

app.run(debug=True)