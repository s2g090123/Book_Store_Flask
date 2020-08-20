from common.database import db

class PurchaseHistory(db.Model):
    __tablename__ = 'puchase_history'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bookName = db.Column(db.String(200), nullable=False)
    storeName = db.Column(db.String(200), nullable=False)
    transactionAmount = db.Column(db.Float, nullable=False)
    transactionDate = db.Column(db.String(200), nullable=False)

    def __init__(self, userId, bookName, storeName, transactionAmount, transactionDate):
        self.userId = userId
        self.bookName = bookName
        self.storeName = storeName
        self.transactionAmount = transactionAmount
        self.transactionDate = transactionDate

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_user_id(cls, userId):
        return cls.query.filter_by(userId=userId).all()

    @classmethod
    def get_most_popular_store_name(cls):
        pass
