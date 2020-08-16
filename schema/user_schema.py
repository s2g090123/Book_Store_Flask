from common.marshmollow import ma
from model.user import User
from schema.purchase_history_schema import PurchaseHistorySchema

class UserSchema(ma.Schema):
    class Mate():
        model = User

    id = ma.Int(required=True)
    name = ma.Str(required=True)
    cashBalance = ma.Float(required=True)
    purchaseHistory = ma.List(ma.Nested(PurchaseHistorySchema))