from common.marshmollow import ma
from model.book import Book

class BookSchema(ma.Schema):
    class Mate:
        model = Book

    # id = ma.Int()
    # bookStoreId = ma.Int()
    bookName = ma.Str(required=True)
    price = ma.Float(required=True)