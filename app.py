from flask import Flask, jsonify, request
from commands import func_fetchall, func_add, func_category, create_table

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/categories')
def cat():
    books1 = func_fetchall('library')
    print('dupa1')
    return jsonify({'categories': [book[1] for book in books1]})


@app.route('/books')
def books():
    cat = func_fetchall('library')
    return jsonify({'books': [book[2] for book in cat]})


@app.route('/IT/')
def cat_IT():
    ITc = func_category('library')
    print(ITc)
    return jsonify({'IT': ITc})


@app.route("/categories/<name>")
def category(name: str):
    return f"Wszystkie książki z kategori: {name}"


@app.route('/add/', methods=['POST'])
def add():
    req = request.get_json()
    category = req['category']
    print(category)
    book = req['book']
    author = req['author']
    pages = req['pages']
    status = req['status']
    print('ABC')
    print(id, category, book, author, pages, status)
    print('ABC')
    func_add('library', category, book, author, pages, status)
    print('dupa1')
    return 'Tutaj zaraz będzie dodawanie'


create_table('Library_new')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# DODAWANIE KOLUMNY DO TABELI PO JEJ UTWORZENIU

# ALTER TABLE table_name ADD COLUMN column_name TIMESTAMP;
