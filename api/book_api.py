from __main__ import app
from flask import request
from model.book import Book
from schema.book_schema import BookSchema

book_schema = BookSchema(many=False)

@app.route('/api/book/list', methods=["GET"])
def get_all_books():
    books = Book.get_all()
    book_list = []
    for book in books:
        book_list.append(book_schema.dump(book))
    return {
        'result': book_list
    }

@app.route('/api/book/get_all_by_price', methods=["GET"])
def getBooksByPrice():
    price = request.args.get('price', type=float)
    books = Book.get_by_price(price)
    book_list = []
    for book in books:
        book_list.append(book_schema.dump(book))
    return {
        'result': book_list
    }

@app.route('/api/book/search', methods=["GET"])
def get_all_by_key_word():
    key_word = request.args.get('keyword', type=str)
    books = Book.get_by_key_word(key_word)
    book_list = []
    for book in books:
        book_list.append(book_schema.dump(book))
    return {
        'result': book_list
    }

@app.route('/api/book/update', methods=["PUT"])
def update_book_by_name():
    params = get_param()
    old_name = params['oldname']
    new_name = params['newname']
    new_price = params.get('newprice', None)
    book = Book.get(old_name)
    if book is None:
        return {
            'result': 'book name is not found.'
        }
    book.bookName = new_name
    if new_price is not None:
        book.price = new_price
    book.update()
    return {
        'result': book_schema.dump(book)
    }

@app.route('/api/book/test', methods=["GET"])
def test():
    book_store_name = request.args.get('store_name', None)
    book_name = request.args.get('book_name', None)
    if book_store_name is None or book_name is None:
        return {
            'result': 'Not found!'
        }
    price = Book.get_price_by_store_name_book_name(book_store_name, book_name)
    print(price)
    return {
        'result': price
    }


def get_param():
    data = request.get_json(force=False)
    if data is None:
        data = request.form
    return data