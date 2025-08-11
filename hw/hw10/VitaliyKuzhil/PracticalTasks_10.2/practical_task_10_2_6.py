def class_name_changer(cls, new_name):
    if not new_name[0].isupper():
        raise NameError('Class name\'s must start with uppercase letter')
    
    if not new_name.isalnum():
        raise NameError('Class name\'s must contain only alphanumeric characters')
    
    cls.__name__ = new_name