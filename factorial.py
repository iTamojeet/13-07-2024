from flask import Flask

app = Flask(__name__)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

@app.route('/factorial/<int:num>')
def get_factorial(num):
    return f"The factorial of {num} is {factorial(num)}"

if __name__ == '__main__':
    app.run(debug=True)