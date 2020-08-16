from __main__ import app
from flask import request
from model.book import Book
from schema.book_schema import BookSchema

book_schema = BookSchema(many=False)

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

def get_param():
    data = request.get_json(force=False)
    if data is None:
        data = request.form
    return data