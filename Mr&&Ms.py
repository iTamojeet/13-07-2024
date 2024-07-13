from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Enter your and your wife's full name in the URL separated by ' / '"

@app.route("/<husband>/<wife>")
def greet(husband, wife):
    return "<h3>Welcome, Mr {} and Ms {}!</h3>".format(husband.lower().capitalize(), wife.lower().capitalize())

app.run(debug=True)