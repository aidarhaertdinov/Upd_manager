from app.model import User
from flask_restful_swagger_3 import Schema


class UserModel(Schema):
    properties = {
        "id": {
            'type': 'integer',
            'format': 'int64',
        },
        "user_name": {
            'type': 'string',
            'format': 'int64',
        },
        "permission": {
            'type': 'string',
            'enum': ['MODERATE', 'ADMIN', 'USER'],
            'format': 'int64',
        }
    }


