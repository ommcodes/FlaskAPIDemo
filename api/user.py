from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.users import Users
from api.error import forbidden


class Users_API(Resource):

    @jwt_required
    def get(self) -> Response:
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            op = Users.objects()
            return jsonify({'result': op})
        else:
            return forbidden()

    @jwt_required
    def delete(self) -> Response:

        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            op = Users.objects.delete()
            return jsonify({'result': op})
        else:
            return forbidden()


class User_API(Resource):

    @jwt_required
    def get(self, user_id: str) -> Response:

        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            op = Users.objects.get(id=user_id)
            return jsonify({'result': op})
        else:
            return forbidden()

    @jwt_required
    def put(self, user_id: str) -> Response:

        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            put_user = Users.objects(id=user_id).update(**data)
            op = {'id': str(put_user.id)}
            return jsonify({'result': op})
        else:
            return forbidden()

    @jwt_required
    def post(self) -> Response:

        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            post_user = Users(**data).save()
            op = {'id': str(post_user.id)}
            return jsonify({'result': op})
        else:
            return forbidden()

    @jwt_required
    def delete(self, user_id: str) -> Response:

        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            op = Users.objects(id=user_id).delete()
            return jsonify({'result': op})
        else:
            return forbidden()
