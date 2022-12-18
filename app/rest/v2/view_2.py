from flask_restful import Resource, reqparse
from app.model import User, db, Permissions

parser = reqparse.RequestParser()  # получает данные
parser.add_argument('user_name', type=str, required=True)  # добавить аргументы
parser.add_argument('password', type=str, required=True)
parser.add_argument('permission', type=str, required=True)

class RestUserList(Resource):
    def get(self):
        users = User.query.all()
        list_users = [user.to_json() for user in users]

        return list_users

class RestUser(Resource):

    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            return user.to_json()
        else:
            return {'сообщение': 'пользователя не существует'}, 404

    def post(self):
        # data = request.get_json()
        data = RestUser.parser.parse_args()
        user = User.from_json(data)
        # user = User(data['user_name'], data['password'], data['permission'])
        session.add(user)
        session.commit()
        return user.to_json(), 201

    def put(self, id):
        # data = request.get_json()
        data = RestUser.parser.parse_args()
        user = User.query.filter_by(id=id).first()
        user.user_name = data.get('user_name') or user.user_name
        user.password = data.get('password') or user.password
        if data.get('permission'):
            user.permission = Permissions.__getitem__(data.get('permission'))
        session.add(user)
        session.commit()
        return user.to_json(), 201


    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            session.delete(user)
            session.commit()
            return {'сообщение': 'пользователь удален'}
        else:
            return {'сообщение': 'пользователя не существует'}, 404



