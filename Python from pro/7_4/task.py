import re

def get_id(names, name):
    pattern = re.compile(r'^[A-Z][a-z]+$')
    if type(name)!= str:
        raise TypeError('Имя не является строкой')
    if bool(pattern.match(name)):
        return ValueError('Имя не является корректным')