def dict_travel(nested_dicts, prefix=''):
    sorted_keys = sorted(nested_dicts.keys())
    for key in sorted_keys:
        if isinstance(nested_dicts[key], dict):
            dict_travel(nested_dicts[key], f"{prefix}{key}.")
        else:
            print(f"{prefix}{key}: {nested_dicts[key]}")

# Примеры использования:

data1 = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
dict_travel(data1)

data2 = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}
dict_travel(data2)

data3 = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}
dict_travel(data3)


# class HourClock:
#     def __init__(self, hours):
#         self.hours = hours
#
#     def get_hours(self):
#         return self._hours
#
#     def set_hours(self, value):
#         if isinstance(value, int) and 1 <= value <= 12:
#             self._hours = value
#         else:
#             raise ValueError('Некорректное время')
#
#     hours = property(get_hours, set_hours)
#
# try:
#     HourClock('pizza time 🕷')
# except ValueError as e:
#     print(e)
# time = HourClock(7)



# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#
#     def set_perimetr(self):
#         return (self.length + self.width) * 2
#
#     def set_area(self):
#         return self.length * self.width
#
#     perimeter = property(set_perimetr)
#     area = property(set_area)
#
# rectangle = Rectangle(4, 5)
#
# print(rectangle.length)
# print(rectangle.width)
# print(rectangle.perimeter)
# print(rectangle.area)

# class ElectricCar:
#     def __init__(self, color):
#         self._color = color
#
#     def get_color(self):
#         return self._color
#
#     def set_color(self, color):
#         self._color = color
#
#     color = property(get_color, set_color)
#
#
# car = ElectricCar('black')
#
# ElectricCar.color.fset(car, 'yellow')
#
# print(car.color)



# class ElectricCar:
#     def __init__(self, color):
#         self._color = color
#
#     def get_color(self):
#         return self._color
#
#     def set_color(self, color):
#         self._color = color
#
#     color = property(get_color, set_color)
#
#
# car = ElectricCar('black')
#
# print(ElectricCar.color.fget())


# def intersperse(iterable, delimiter):
#     it = iter(iterable)
#     yield next(it)
#     for element in it:
#         yield delimiter
#         yield element

# inter = intersperse('beegeek', '!')
# print(next(inter))
# print(next(inter))
# print(*inter)
#
#
# print(*intersperse([1, 2, 3], 0))
# class BankAccount:
#     def __init__(self, balance=0):
#         self._balance = balance
#
#     def get_balance(self):
#         return self._balance
#
#     def deposit(self, amount):
#         self._balance += amount
#
#     def withdraw(self, amount):
#         if amount > self._balance:
#             raise ValueError("На счете недостаточно средств")
#         self._balance -= amount
#     def transfer(self, account, amount):
#         if amount > self._balance:
#             raise ValueError("На счете недостаточно средств")
#         self._balance -= amount
#         account.deposit(amount)
#
#
# account = BankAccount()
#
# print(account.get_balance())
# account.deposit(100)
# print(account.get_balance())
# account.withdraw(50)
# print(account.get_balance())


# from math import pi
#
#
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#         self._diameter = radius * 2
#         self._area = pi * radius ** 2
#
#     def get_radius(self):
#         return self._radius
#
#     def get_diameter(self):
#         return self._diameter
#
#     def get_area(self):
#         return self._area
#
#
#
# circle = Circle(1)
#
# print(circle.get_radius())
# print(circle.get_diameter())
# print(round(circle.get_area()))