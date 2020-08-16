from common.marshmollow import ma
from model.book_store import BookStore
from schema.book_schema import BookSchema

class BookStoreSchema(ma.Schema):
    class Mate:
        model = BookStore

    # id = ma.Int()
    cashBalance = ma.Float(required=True)
    openingHours = ma.Str(required=True)
    storeName = ma.Str(required=True)
    books = ma.List(ma.Nested(BookSchema))