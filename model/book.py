from common.database import db

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