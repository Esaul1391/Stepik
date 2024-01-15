from functools import singledispatchmethod


class ElectricCar:
    @singledispatchmethod
    def __init__(self, color):
        raise ValueError

    @__init__.register(str)
    def _from_str(self, color):
        self.color = color

    @__init__.register(list)
    def _from_list_tuple(self, color):
        self.color = ', '.join(color)


car1 = ElectricCar('yellow')
car2 = ElectricCar(['black', 'white'])

print(car1.color)
print(car2.color)




# class StrExtension:
#
#
#     @staticmethod
#     def remove_vowels(string):
#         vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
#         return ''.join(i for i in string.split() if i not in vowels)
#
#     @staticmethod
#     def leave_alpha(s):
#         return ''.join(i for i in s if i in i.isalpha())
#
#     @staticmethod
#     def replace_all(string, chars, char):
#         s = string.replace(chars, char)
#         return s



# class Pet:
#     pets_list = []
#     def __init__(self, name):
#         self.name = name
#         Pet.pets_list.append(self)
#     @classmethod
#     def first_pet(cls):
#         return cls.pets_list[0] if cls.pets_list else None
#
#     @classmethod
#     def last_pet(cls):
#         return cls.pets_list[-1] if cls.pets_list else None
#
#     @classmethod
#     def num_of_pets(cls):
#         return len(cls.pets_list)




# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     @classmethod
#     def from_iterable(cls, cof):
#         return cls(*cof)
#
#     @classmethod
#     def from_str(cls, cof_str):
#         coefficients = [float(i) for i in cof_str.split()]
#         return cls(*coefficients)
#
# polynom = QuadraticPolynomial(1, -5, 6)
#
# print(polynom.a)
# print(polynom.b)
# print(polynom.c)


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     @classmethod
#     def square(cls, side):
#         return cls(side, side)
#
# rectangle = Rectangle.square(5)
#
# print(rectangle.length)
# print(rectangle.width)

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @classmethod
#     def from_diameter(cls, diameter):
#         return cls(diameter/2)
#
# circle = Circle.from_diameter(10)
#
# print(circle.radius)

# class ElectricCar:
#     def __init__(self, color):
#         if not ElectricCar.is_valid(color):
#             raise ValueError
#         self._color = color
#
#     @staticmethod
#     def is_valid(data):
#         return isinstance(data, str) and data.isalpha()
#
#
# car = ElectricCar('black')
#
# print(ElectricCar.is_valid(car, 'yellow'))