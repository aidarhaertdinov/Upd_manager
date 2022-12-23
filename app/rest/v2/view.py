from flask_restful_swagger_3 import swagger, Resource
from flask_restful.reqparse import RequestParser
from app.model import User, Permissions, db
from app.resource.swagger_schema.v2.schema import UserModel
from app import csrf
from flask import session, request


class RestUserList(Resource):
    @swagger.tags('user')
    @swagger.reorder_with(UserModel, description="Returns a user")
    def get(self):
        users = User.query.all()
        list_users = [user.to_json() for user in users]

        return list_users, 200

class RestUser(Resource):
    parser = RequestParser()  # получает данные
    parser.add_argument('user_name', type=str, required=True)  # добавить аргументы
    parser.add_argument('password', type=str, required=True)
    parser.add_argument('permission', type=str, required=True)
    @swagger.tags('user')
    @swagger.reorder_with(UserModel, description="Returns a user")
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            return user.to_json()
        else:
            return {'сообщение': 'пользователя не существует'}, 404

    @csrf.exempt
    @swagger.tags('user')
    @swagger.reorder_with(UserModel, description="Returns a user")
    def post(self):
        data = request.get_json()
        # data = RestUser.parser.parse_args()
        user = User.from_json(data)
        # user = User(data['user_name'], data['password'], data['permission'])
        db.session.add(user)
        db.session.commit()
        return user.to_json(), 201

    @csrf.exempt
    @swagger.tags('user')
    @swagger.reorder_with(UserModel, description="Returns a user")
    def put(self, id):
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

    @csrf.exempt
    @swagger.tags('user')
    @swagger.reorder_with(UserModel, description="Returns a user")
    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'сообщение': 'пользователь удален'}
        else:
            return {'сообщение': 'пользователя не существует'}, 404



