from flask import Flask

app = Flask(__name__)

book_list = ["java with bluej", "let us c", "eloquent javascript", "python playground", "###"]

@app.route('/')
def index():
    display = ""
    for book in book_list:
        display += "<p>" + book + "</p>"
    return display

if __name__ == '__main__':
    app.run(debug=True)