from __main__ import app
from flask import request
from model.user import User
from schema.user_schema import UserSchema
from schema.purchase_history_schema import PurchaseHistorySchema
from model.book_store import BookStore
from model.book import Book
from model.purchase_history import PurchaseHistory

user_schema = UserSchema(many=False)
purchage_history_schema = PurchaseHistorySchema(many=False)

@app.route('/api/user/list', methods=["GET"])
def get_all_users():
    users = User.get_all()
    user_list = []
    for user in users:
        user_list.append(user_schema.dump(user))
    return {
        'result': user_list
    }

@app.route('/api/user/insert', methods=["POST"])
def insert_user():
    params = get_param()
    user_name = params['name']
    user_cash = params['cash']
    user = User(user_name, user_cash)
    user.insert()
    return {
        'result': 'Insert done!'
    }

@app.route('/api/user/update', methods=["PUT"])
def update_user_by_name():
    params = get_param()
    old_name = params['oldname']
    new_name = params['newname']
    user = User.get_by_name(old_name)
    if user is None:
        return {
            'result': 'User is not found.'
        }
    user.name = new_name
    user.update()
    return {
        'result': user_schema.dump(user)
    }

@app.route('/api/user/buy', methods=["POST"])
def user_buy_book():
    params = get_param()
    book_store_name = params.get('book_store_name', None)
    book_name = params.get('book_name', None)
    user_id = params.get('id', None)
    if book_store_name is None or book_name is None or user_id is None:
        return {
            'result': 'Error!'
        }
    book_store = BookStore.get(book_store_name)
    if book_store is None:
        return {
            'result': 'Book Store is not found!'
        }
    price = Book.get_price_by_store_name_book_name(book_store.storeName, book_name)
    if price is None:
        return {
            'result': 'Book is not found!'
        }
    user = User.get_by_id(user_id)
    if user is None:
        return {
            'result': 'User is not found!'
        }
    user.cashBalance -= price[0]
    book_store.cashBalance += price[0]
    user.update()
    book_store.update()
    purchase = PurchaseHistory(user_id, book_name, book_store_name, price[0], "today")
    purchase.insert()
    return {
        'result': purchage_history_schema.dump(purchase)
    }

def get_param():
    data = request.get_json(force=False)
    if data is None:
        data = request.form
    return data