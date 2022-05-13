from flask_restful import Api
from api.product import Products_API, Product_API
from api.auth import Login_API, register_API
from api.user import User_API, Users_API


def makeroute(api: Api):

    api.add_resource(Products_API, '/product/')
    api.add_resource(register_API, '/auth/register/', methods=['POST'])
    api.add_resource(Login_API, '/auth/login/')
    api.add_resource(Users_API, '/user/')
    api.add_resource(User_API, '/user/<user_id>')
    api.add_resource(Product_API, '/product/<barcode>')
