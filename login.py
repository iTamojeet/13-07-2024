from flask import Flask

app = Flask(__name__)

@app.route('/<username>/<password>')
def checkuser(username,password):
    if username == "python" and password == "flask":
        return "<h3>Welcome to the python flask app!!!</h3>"
    else:
        return "<h3>Invalid username or password. Try again...</h3>"

if __name__ == '__main__':
    app.run(debug=True)