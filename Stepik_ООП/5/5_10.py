class AlwaysEquals:
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        return True

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return f'AlwaysEquals({repr(self.data)})'


data = {}
obj1 = AlwaysEquals('bee')
obj2 = AlwaysEquals('geek')

data[obj1] = 'пчела'
data[obj2] = 'гик'

print(data)


# from time import perf_counter
#
#
# def search_time_test(collection, numbers):
#     start = perf_counter()
#
#     for num in numbers:
#         num in collection
#
#     end = perf_counter()
#     return end - start
#
#
# numbers = range(10000)
#
# d = dict(zip(numbers, numbers))
# s = set(numbers)
# l = list(numbers)
#
# print(search_time_test(d, numbers))  # результат в секундах
# print(search_time_test(s, numbers))  # результат в секундах
# print(search_time_test(l, numbers))





# class ColoredPoint:
#     def __init__(self, x, y, color):
#         self._x = x
#         self._y = y
#         self._color = color
#
#     def __repr__(self):
#         return f"ColoredPoint({self._x}, {self._y}, '{self._color}')"
#
#     def __eq__(self, other):
#         if isinstance(other, ColoredPoint):
#             return self._x == other._x, self._y == other._y, self._color == other._color
#         return NotImplemented
#
#     def __hash__(self):
#         return hash(self._fields)
#
#     def _fields(self):
#         return self._x, self._y, self._color
#
#
#     @property
#     def x(self):
#         return self._x
#
#     @property
#     def y(self):
#         return self._y
#
#     @property
#     def color(self):
#         return self._color