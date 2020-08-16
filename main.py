from flask import Flask
from flask_restful import Api, Resource
from flask_migrate import Migrate

from common import database, marshmollow

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_storm.db'

api = Api(app)
database.init_db(app)
marshmollow.init_ma(app)

from api import book_store_api, book_api

if __name__ == "__main__":
    migrate = Migrate(app, database.db)
    migrate.db.create_all()
    app.run()