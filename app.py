from flask import Flask, jsonify, request
from commands import func_fetchall, func_add, func_category, create_table
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, Welcome to library</p>"


@app.route('/categories')
def cat():
    books = func_fetchall('library')
    return jsonify({'categories': [book[1] for book in books]})


@app.route('/books')
def books():
    try:
        cat = func_fetchall('library')
        return jsonify({'books': [book[2] for book in cat]})
    except:
        print("Can't establish a connection to the database. Please check db's configuration")


@app.route('/IT/')
def cat_IT():
    ITc = func_category('library')
    return jsonify({'IT': ITc})


@app.route("/categories/<name>")
def category(name: str):
    return f"Wszystkie książki z kategori: {name}"

#


@app.route('/add/', methods=['POST'])
def add():
    req = request.get_json()
    category = req['category']
    book = req['book']
    author = req['author']
    pages = req['pages']
    status = req['status']
    func_add('library', category, book, author, pages, status)
    return 'Tutaj zaraz będzie dodawanie'

####################################################################################################


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

####################################################################################################


#create_table('Library')

'''
payload = {
    "category": "IT",
    "book": "Linux wprowadzenie do języka poleceń",
    "author": "Kent Beck",
    "pages": 500,
    "status": "to read"
}

#r = requests.put('https://httpbin.org/post', data=payload)
r = requests.put('http://localhost:5000/add/', params=payload)

print(r.text)
'''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# DODAWANIE KOLUMNY DO TABELI PO JEJ UTWORZENIU

# ALTER TABLE table_name ADD COLUMN column_name TIMESTAMP;
