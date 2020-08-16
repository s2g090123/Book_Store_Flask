from common.marshmollow import ma
from model.purchase_history import PurchaseHistory

class PurchaseHistorySchema(ma.Schema):
    class Mate():
        model = PurchaseHistory

    bookName = ma.Str(required=True)
    storeName = ma.Str(required=True)
    transactionAmount = ma.Float(required=True)
    transactionDate = ma.Str(required=True)