from flask_restful import Resource, reqparse
from app.model import User


class RestMain(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            return user.json()
        else:
            return {'сообщение': 'пользователя не существует'}, 404

    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            session.delete(user)
            session.commit()
            return {'сообщение': 'пользователь удален'}
        else:
            return {'сообщение': 'пользователя не существует'}, 404


    def post(self, id):
        data = request.get_json()
        user = User(data['user_name'], data['password'], data['permission'])
        session.add(user)
        session.commit()
        return user.json(), 201

        # parser = reqparse.RequestParser() # получает данные
        # parser.add_argument('user_name', type=str) # добавить аргументы
        # parser.add_argument('password', type=str)
        # parser.add_argument('permission', type=str)
        # data = RestMain.parser.parse_args()

    def put(self, id):
        data = request.get_json()
        user = User.query.filter_by(id=id).first()
        if user:
            user.user_name = data['user_name']
            user.password = data['password']
            user.permission = data['permission']
        session.add(user)
        session.commit()
        return user.json(), 201
