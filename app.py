from flask import Flask, app
from flask_mongoengine import MongoEngine
from api.routes import makeroute
from flask_jwt_extended import JWTManager
from flask_restful import Api
import os

# Configuration for MongoDB (Default)

mdbConfig = {'MONGODB_SETTINGS': {
    'db': 'GroceryData',
    'host': 'localhost',
    'port': 27017,
    'authentication_source': 'admin',
    'username': 'admin',
    'password': 'password'},
    'JWT_SECRET_KEY': 'Have to input from Postman'}


def get_app(config: dict = None) -> app.Flask:
    # initiate flask
    flask_app = Flask(__name__)
    flask_app.url_map.strict_slashes = False
    # app configuration
    config = mdbConfig if config is None else config
    flask_app.config.update(config)
    if 'MONGODB_URI' in os.environ:
        flask_app.config['MONGODB_SETTINGS'] = {'host': os.environ['MONGODB_URI'], 'retryWrites': False}
    if 'JWT_SECRET_KEY' in os.environ:
        flask_app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
    api = Api(app=flask_app)
    makeroute(api=api)
    db = MongoEngine(app=flask_app)
    jwt = JWTManager(app=flask_app)

    return flask_app


if __name__ == '__main__':
    # first entry
    app = get_app()
    app.run(debug=True)
