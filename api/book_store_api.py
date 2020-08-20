from __main__ import app
from flask import request
from model.book_store import BookStore
from model.book import Book
from schema.book_store_schema import BookStoreSchema

book_store_schema = BookStoreSchema(many=False)

@app.route('/api/book_store/list_by_time', methods=["GET"])
def getBookStoreByTime():
    time = request.args.get('time', type=str)
    book_stores = BookStore.get_all_by_time(time)
    book_store_list = []
    for book_store in book_stores:
        book_store_list.append(book_store_schema.dump(book_store))
    return {
        'result': book_store_list
    }

@app.route('/api/book_store/list', methods=["GET"])
def getAllBookStores():
    book_stores = BookStore.get_all()
    book_store_list = []
    for book_store in book_stores:
        book_store_list.append(book_store_schema.dump(book_store))
    return {
        'result': book_store_list
    }

@app.route('/api/book_store/insert', methods=["POST"])
def insertBookStore():
    params = book_store_schema.load(get_param())
    book_store = BookStore(params['storeName'], params['cashBalance'], params['openingHours'])
    book_store.insert()
    return {
        'message': 'Insert done!'
    }

@app.route('/api/book_store/insert_book', methods=["POST"])
def insertBook():
    params = get_param()
    store = BookStore.get(params['storeName'])
    book = Book(store.id, params["bookName"], params["price"])
    book.insert()
    return {
        "message": "Insert done!"
    }

@app.route('/api/book_store/list_by_book_count', methods=["GET"])
def get_by_book_count():
    count = request.args.get('count', type=int)
    is_greater = request.args.get('greater', tpye=bool)
    stores = BookStore.get_all_by_count(count, is_greater)
    store_list = []
    for store in stores:
        store_list.append(book_store_schema.dump(store))
    return {
        "result": store_list
    }

@app.route('/api/book_store/list_by_book_price_count', methods=["GET"])
def get_by_book_price_count():
    price = request.args.get('price', type=float)
    count = request.args.get('count', type=int)
    is_greater = request.args.get('greater', type=bool)
    stores = BookStore.get_all_by_price_and_count(price, count, is_greater)
    store_list = []
    for store in stores:
        store_list.append(book_store_schema.dump(store))
    return {
        "result": store_list
    }

@app.route('/api/bookstore/search', methods=["GET"])
def get_by_key_word():
    key_word = request.args.get('keyword', type=str)
    stores = BookStore.get_all_by_key_word(key_word)
    store_list = []
    for store in stores:
        store_list.append(book_store_schema.dump(store))
    return {
        "result": store_list
    }

@app.route('/api/bookstore/update', methods=["PUT"])
def update_book_store_by_name():
    params = get_param()
    query = BookStore.get(params['oldname'])
    if query is None:
        return {
            'result': 'book store is not found.'
        }
    query.storeName = params['newname']
    query.update()
    store = book_store_schema.dump(query)
    return {
        "result": store
    }


def get_param():
    data = request.get_json(force=False)
    if data is None:
        data = request.form
    return data