from flask import Flask

app = Flask(__name__)

lists = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]]

@app.route('/<int:list_index>')
def index(list_index):
    selected_list = lists[list_index]
    return f"Selected list: {selected_list} and it's index: {list_index}"

if __name__ == '__main__':
    app.run(debug=True)