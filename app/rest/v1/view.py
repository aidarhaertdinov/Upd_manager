from app.rest import rest_v1
from app.model import User, db, Permissions, Enum
from flask import jsonify, request, session


@rest_v1.route("/api/users", methods=['GET'])
def get_users():
    users = User.query.all()
    list_users = [user.to_json() for user in users]

    return jsonify(list_users)


@rest_v1.route("/api/users/<int:id>", methods=['GET'])
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return {'message': 'нету пользователя с таким id'}, 400

    return jsonify(user.to_json())


@rest_v1.route("/api/users", methods=['POST'])
def post_user():
    data = request.get_json()
    user = User.from_json(data)
    db.session.add(user)
    db.session.commit() # вернуть сохраненного пользователя в момент комита
    return jsonify(user.to_json())

@rest_v1.route("/api/users/<int:id>", methods=['PUT'])
def put_user(id):
    data = request.get_json()
    user = User.query.filter_by(id=id).first()
    user.user_name = data['user_name']
    user.password = data['password']
    user.permission = data['permission']
    # user = update_user.from_json(data)
    if not user:
        return {'message': 'нету пользователя с таким id'}, 400
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_json())


@rest_v1.route("/api/users/<int:id>", methods=['DELETE'])
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return {'message': 'нету пользователя с таким id'}, 400
    db.session.delete(user)
    db.session.commit()
    return {'сообщение': 'пользователь удален'}
