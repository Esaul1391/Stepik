from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress):
        self.ipaddress = ipaddress

    @__init__.register(tuple)
    @__init__.register(list)
    def _from_list_otr_tuple(self, data):
        self.ipaddress = '.'.join(map(str, data))

    def __str__(self):
        return self.ipaddress

    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"


sp = (1, 1, 11, 11)
print('.'.join(map(str, sp)))

# class Vector:
#     def __init__(self, x ,y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'Вектор на плоскости с координатами ({self.x}, {self.y})'
#
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def __str__(self):
#         return f'Rectangle({self.length}, {self.width})'
#
#     def __repr__(self):
#         return f'Rectangle({self.length}, {self.width})'


# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def __str__(self):
#         return f'{self.title} ({self.author}, {self.year})'
#
#     def __repr__(self):
#         return f"Book('{self.title}', '{self.author}', {self.year})"
