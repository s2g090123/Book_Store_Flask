from flask_marshmallow import Marshmallow

ma = None

def init_ma(app):
    global ma
    ma = Marshmallow(app)