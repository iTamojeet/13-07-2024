from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Enter two numbers in the URL separated by ' / '"

@app.route("/<int:num1>/<int:num2>")
def add(num1, num2):
    return f"Sum of {num1} and {num2} is: {num1+num2}"

app.run(debug=True)