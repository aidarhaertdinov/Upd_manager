from flask_admin.contrib.fileadmin import FileAdmin


class FileAdminView(FileAdmin):
    column_exclude_list = ['name', 'size', 'date']
    column_labels = {
        "name": "Название",
        "size": "Размер",
        "date": "Дата",
    }
    can_delete = True
    can_rename = True
    edit_modal = True
    create_modal = True
