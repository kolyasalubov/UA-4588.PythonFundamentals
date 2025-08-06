def class_name_changer(cls, new_name):
    if new_name and new_name[0].isupper() and new_name.isidentifier() and not new_name[0].isdigit():
        cls.__name__ = new_name