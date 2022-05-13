# flask

from flask import Response, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource
from models.users import Users
from api.error import unauth
import datetime


class register_API(Resource):

    @staticmethod
    def post() -> Resource:
        data = request.get_json()
        post_usr = Users(**data)
        post_usr.save()
        op = {'id': str(post_usr.id)}
        return jsonify({'result': op})


class Login_API(Resource):

    @staticmethod
    def post() -> Response:
        data = request.get_jason()
        user = Users.object.get(email=data.get('email'))
        authentication_success = user.chk_pwd(data.get('password'))

        if not authentication_success:
            return unauth()
        else:
            expiry = datetime.timedelta(days=5)
            access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
            refresh_token = create_refresh_token(identity=str(user.id))
            return jsonify({'result' : {'access_token': access_token,
                                        'refresh_token': refresh_token,
                                        'logged_in_as': f"{user.email}"}})
