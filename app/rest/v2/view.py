from flask_restful_swagger_3 import swagger, Resource
from flask_restful.reqparse import RequestParser
from app.model import User, Permissions, db
from app.resource.swagger_schema.v2.schema import UserModel
from app import csrf
from flask import request
from ..errors import errors

class RestUserList(Resource):
    @swagger.tags('user')
    @swagger.reorder_with(UserModel, description="Returns a user")
    def get(self):
        try:
            users = User.query.all()
            list_users = [user.to_json() for user in users]
            return list_users, 200

        except AttributeError:
            return errors.get('UserNotFound'), errors.get('UserNotFound').get('status')

class RestUser(Resource):
    parser = RequestParser()  # получает данные
    parser.add_argument('user_name', type=str, required=True)  # добавить аргументы
    parser.add_argument('password', type=str, required=True)
    parser.add_argument('permission', type=str, required=True)
    @swagger.tags('user')
    @swagger.reorder_with(UserModel, description="Returns a user")
    def get(self, id):
        try:
            user = User.query.filter_by(id=id).first()
            return user.to_json()

        except AttributeError:
            return errors.get('UserNotFound'), errors.get('UserNotFound').get('status')

    @csrf.exempt
    @swagger.tags('user')
    @swagger.reorder_with(UserModel, description="Returns a user")
    def post(self):
        try:
            data = request.get_json()
            # data = RestUser.parser.parse_args()
            user = User.from_json(data)
            db.session.add(user)
            db.session.commit()
            return user.to_json(), 201
        except AttributeError:
            return errors.get('PasswordNotFound'), errors.get('PasswordNotFound').get('status')
        except KeyError:
            return errors.get('PermissionNotFound'), errors.get('PermissionNotFound').get('status')

    @csrf.exempt
    @swagger.tags('user')
    @swagger.reorder_with(UserModel, description="Returns a user")
    def put(self, id):
        try:
            data = request.get_json()
            # data = RestUser.parser.parse_args()
            user = User.query.filter_by(id=id).first()
            user.user_name = data.get('user_name') or user.user_name
            user.password = data.get('password') or user.password
            if data.get('permission'):
                user.permission = Permissions.__getitem__(data.get('permission'))
            db.session.add(user)
            db.session.commit()
            return user.to_json(), 201

        except AttributeError:
            return errors.get('UserNotFound'), errors.get('UserNotFound').get('status')
    @csrf.exempt
    @swagger.tags('user')
    @swagger.reorder_with(UserModel, description="Returns a user")
    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return errors.get('UserNotFound'), errors.get('UserNotFound').get('status')
        db.session.delete(user)
        db.session.commit()
        return {'сообщение': 'пользователь удален'}



