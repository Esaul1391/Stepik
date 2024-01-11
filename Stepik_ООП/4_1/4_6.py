# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @property
#     def fullname(self):
#         return self.name + ' ' + self.surname
#
#     @fullname.setter
#     def fullname(self, fullname):
#         self.name, self.surname = fullname.split()
#
# person = Person('Mike', 'Pondsmith')
#
# person.name = 'Troy'
# print(person.fullname)


class Account:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def hash_function(password):
        hash_value = 0
        for char, index in zip(password, range(len(password))):
            hash_value += ord(char) * index
        return hash_value % 10 ** 9

    @property
    def login(self):
        return self.login

    @login.setter
    def login(self, value):
        raise AttributeError

    @property
    def password(self):
        return hash_function(self.password)

