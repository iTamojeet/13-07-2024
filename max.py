from flask import Flask

app = Flask(__name__)

@app.route('/max')
def maximum():
    numbers = [10,15,77,33,99,85,26,1,000,64,50,37,79,69,19,2]
    return f"Max value in thi slist is: {max(numbers)}"

if __name__ == '__main__':
    app.run(debug=True)