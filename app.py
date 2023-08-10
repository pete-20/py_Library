from flask import Flask, jsonify, request
import commands as cms
import psycopg2.errors as db_err

app = Flask(__name__)


# 1
@app.route("/API")
def hello_world():
    info = ("<h1>Hello, Welcome to Pete's library</h1>"
            "<p>############################   API's interface - available endpoints:   ############################</p>"
            "<p>http://localhost:5000/API/ ---> landging page <p>"
            "<p>http://localhost:5000/API/categories ---> available categories</p>"
            "<p>http://localhost:5000/API/books ---> available books</p>"
            "<p>DELETE http://localhost:5000/API/books/<id> ---> deleting an object with <id></p>"
            "<p>PUT http://localhost:5000/API/books/<id> ---> updating an object with <id></p>"
            "<p>GET http://localhost:5000/API/books/<id> --> getting information about an object with <id></p>"
            "<p>http://localhost:5000/API/<category> --> all available books from <category></p>"
            "<p>http://localhost:5000/API/add --> adding a new book</p>"
            "<p>{</p>"
            "<p>'category': str,</p>"
            "<p>'book': str,</p>"
            "<p>'author': str,</p>"
            "<p>'pages': int,</p>"
            "<p>'status': str</p>"
            "<p>}</p>"
            )
    return info


# 2
@app.route('/API/categories')
def categories():
    books = cms.func_category_distinct('library')
    return jsonify({'categories': [book[0] for book in books]}), 200


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
                books3 = cms.func_book_id('library', id)
                return jsonify({f'Book ID: {id}': [book for book in books3]})
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


@app.route('/API/<category>')
def cat_IT(category):
    categ = cms.func_category('library', category)
    return jsonify(
        {f"All books from category {category}": [cat1[2] for cat1 in categ]})


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
        return f"{book} succesfully added to the databse!"
    except db_err.UniqueViolation:
        return f"Value {book} duplicated. Can't save the same book second time"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
