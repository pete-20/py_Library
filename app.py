from flask import Flask, jsonify, request
import commands as cms
import psycopg2.errors as db_err

app = Flask(__name__)


@app.route("/API/")
def hello_world():
    return "<p>Hello, Welcome to Pete's library</p>"


@app.route('/API/categories')
def categories():
    books = cms.func_category_distinct('library')
    return jsonify({'books': [book[0] for book in books]}), 200



@app.route('/API/books')
def books():
    try:
        cat = cms.func_fetchall('library')
        return jsonify({'books': [book[2] for book in cat]}), 200
    except:
        print("Can't establish a connection to the database.\n")
        print("Please check db's configuration.")


@app.route('/API/books/<id>', methods=['DELETE', 'GET', 'PUT'])
def book_id(id):
    try:
        if request.method == 'GET':
            try:
                books3 = cms.func_fetchall('library')
                return jsonify({'All books': [book[1] for book in books3]})
            except:
                return f"Can't show book ID - {id}"
        elif request.method == 'DELETE':
            try:
                cms.func_delete('library', id)
                return f"Deleted id: {id}"
            except:
                return f"Can't delete ID: {id}"
        elif request.method == 'PUT':
            try:
                req = request.get_json()
                key_to_update = [req_key for req_key in req.keys()][0]
                value_to_update = [req_value for req_value in req.values()][0]
                cms.func_update('library', key_to_update, value_to_update, id)
                return jsonify(f"Message: Book - ID:{id} succesfully updated")
            except:
                return f"Can't update Book - ID: {id}"
    except:
        return print("Can't connect")


@app.route('/API/IT/')
def cat_IT():
    ITc = cms.func_category('library', 'IT')
    return jsonify({'IT': ITc})


@app.route("/API/categories/<name>")
def category(name: str):
    return f"Wszystkie książki z kategori: {name}"


@app.route('/API/add', methods=['POST'])
def add():
    try:
        req = request.get_json()
        category = req['category']
        book = req['book']
        author = req['author']
        pages = req['pages']
        status = req['status']
        cms.func_add('library', category, book, author, pages, status)
        return 'Tutaj zaraz będzie dodawanie'
    except db_err.UniqueViolation:
        return f"Value {book} duplicated. Can't save the same book second time"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
