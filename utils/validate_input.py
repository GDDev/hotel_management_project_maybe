import re

from utils.custom_exceptions import InvalidInputError

def validate_name(full_name):
    pattern = r'^[a-zA-Z ]+$' 
    if re.match(pattern, full_name) is not None:
        full_name = full_name.upper().split(' ')
        name = full_name[0]
        last_name = full_name[1:len(full_name)]
        last_name = ' '.join(last_name)
        return (name, last_name)
    raise InvalidInputError('O nome deve conter apenas letras.')

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email) is None:
        raise InvalidInputError('Formato de e-mail inválido.')

def validate_username(username):
    pattern = r'^[a-zA-Z0-9_-]+$'
    if re.match(pattern, username) is None:
        raise InvalidInputError('Username deve ser alfanumérico.')
