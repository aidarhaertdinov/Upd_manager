from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    column_exclude_list = ['password', ]
    column_labels = {
        "id": "ID",
        "user_name": "Имя пользователя",
        "password": "Пароль",
        "permission": "Роль"
    }
    column_default_sort = ("user_name", False)
    column_searchable_list = ["user_name"]
    column_editable_list = ["user_name",'permission']
    create_modal = True
    edit_modal = True