# packages for flask

from flask import jsonify, request, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# MongoEngine models

from models.products import Products

# resources
from models.products import Products
from models.users import Users
from api.error import forbidden


class Products_API(Resource):

    @jwt_required()
    def get(self) -> Response:
        op = Products.objects()
        return jsonify({'result': op})

    @jwt_required()
    def post(self) -> Response:
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin
        if authorized:
            data = request.get_json()
            post_user = Products(**data).save()
            op = {'id': str(post_user.id)}
            return jsonify({'result': op})
        else:
            return forbidden()


class Product_API(Resource):

    @jwt_required
    def get(self, barcode: str) -> Response:
        op = Products.objects.get(id=barcode)
        return jsonify({'result': op})

    @jwt_required
    def put(self, barcode: str) -> Response:
        data = request.get_json()
        put_user = Products.objects(id=barcode).update(**data)
        return jsonify({'result': put_user})

    @jwt_required
    def delete(self, user_id: str) -> Response:
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Products.objects(id=user_id).delete()
            return jsonify({'result': output})
        else:
            return forbidden()
