from common.database import db
from model.book import Book
from sqlalchemy import func

class BookStore(db.Model):
    __tablename__ = 'book_store'
    id = db.Column(db.Integer, primary_key=True)
    cashBalance = db.Column(db.Float, nullable=False)
    openingHours = db.Column(db.String(200), nullable=False)
    storeName = db.Column(db.String(120), nullable=False)
    books = db.relationship('Book', backref='book_store', lazy=True)

    def __init__(self, storeName, cashBalance, openingHours):
        self.storeName = storeName
        self.cashBalance = cashBalance
        self.openingHours = openingHours

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get(cls, storeName):
        return cls.query.filter_by(storeName=storeName).first()

    @classmethod
    def get_all_by_time(cls, time):
        return cls.query.filter_by(openingHours=time).all()

    @classmethod
    def get_all_by_count(cls, count, isGreater):
        book_count = (func.count(cls.id)).label("book_count")
        if (isGreater == True):
            return cls.query. \
                join(Book, cls.id == Book.bookStoreId).group_by(cls.id).having(book_count > count).all()
        else:
            return db.session.query(cls) \
            .join(Book, cls.id == Book.bookStoreId).group_by(cls.id).having(book_count < count).all()

    @classmethod
    def get_all_by_price_and_count(cls, price, count, isGreater):
        book_count = (func.count(cls.id)).label("book_count")
        if (isGreater == True):
            return cls.query.join(Book, cls.id == Book.bookStoreId). \
                filter(Book.price <= price).group_by(cls.id).having(book_count > count).all()
        else:
            return cls.query.join(Book, cls.id == Book.bookStoreId). \
                filter(Book.price <= price).group_by(cls.id).having(book_count < count).all()

    @classmethod
    def get_all_by_key_word(cls, keyword):
        search = "%{}%".format(keyword)
        return cls.query.filter(cls.storeName.like(search)).order_by(cls.storeName).all()

    @classmethod
    def get_all(cls):
        return cls.query.all()