from common.database import db
from model import book_store

class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    bookStoreId = db.Column(db.Integer, db.ForeignKey('book_store.id'), nullable=False)
    bookName = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, bookStoreId, bookName, price):
        self.bookStoreId = bookStoreId
        self.bookName = bookName
        self.price = price

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get(cls, bookName):
        return cls.query.filter_by(bookName=bookName).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_price(cls, price):
        return cls.query.filter(cls.price <= price).order_by(cls.price, cls.bookName).all()

    @classmethod
    def get_by_key_word(cls, key_word):
        search = "%{}%".format(key_word)
        return cls.query.filter(cls.bookName.like(search)).order_by(cls.bookName).all()

    @classmethod
    def get_price_by_store_name_book_name(cls, store_name, book_name):
        return db.session.query(cls.price).join(book_store.BookStore, cls.bookStoreId == book_store.BookStore.id). \
            filter(book_store.BookStore.storeName == store_name, cls.bookName == book_name).first()

