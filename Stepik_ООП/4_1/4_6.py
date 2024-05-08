

class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode
        self.r = 0
        self.g = 0
        self.b = 0











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

#
# class Account:
#     def __init__(self, login, password):
#         self.login = login
#         self.password = password
#
#     def hash_function(password):
#         hash_value = 0
#         for char, index in zip(password, range(len(password))):
#             hash_value += ord(char) * index
#         return hash_value % 10 ** 9
#
#     @property
#     def login(self):
#         return self.login
#
#     @login.setter
#     def login(self, value):
#         raise AttributeError
#
#     @property
#     def password(self):
#         res = self.hash_function(self.password)
#         return res
#
#     @password.setter
#     def password(self, value):
#         self.password = value
# account = Account('hannymad', 'cakeisalie')
#
# print(account.login)
# print(account.password)


# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.__calculate_roots()
#
#     def __calculate_roots(self):
#         discriminant = self.b ** 2 - 4 * self.a * self.c
#         if discriminant >= 0:
#             sqrt_discriminant = discriminant ** 0.5
#             self.__x1 = (-self.b - sqrt_discriminant) / (2 * self.a)
#             self.__x2 = (-self.b + sqrt_discriminant) / (2 * self.a)
#         else:
#             self.__x1 = None
#             self.__x2 = None
#
#     @property
#     def x1(self):
#         return self.__x1
#
#     @property
#     def x2(self):
#         return self.__x2
#
#     @property
#     def view(self):
#         if self.c >= 0:
#             return f'{self.a}x^2 + {self.b}x + {self.c}'
#         else:
#             return f'{self.a}x^2 + {self.b}x - {abs(self.c)}'
#
#     @property
#     def coefficients(self):
#         return (self.a, self.b, self.c)
#
#     @coefficients.setter
#     def coefficients(self, value):
#         self.a, self.b, self.c = value
#         self.__calculate_roots()