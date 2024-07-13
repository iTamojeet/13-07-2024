from flask import Flask

app = Flask(__name__)

@app.route('/sort')
def sort_numbers():
    numbers = [10,15,77,33,99,85,26,1,000,64,50,37,79,69,19,2]
    sorted_numbers = sorted(numbers)
    return f"Sorted numbers: {sorted_numbers}"

if __name__ == '__main__':
    app.run(debug=True)