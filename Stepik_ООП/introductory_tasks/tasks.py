class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def set_name(self, n):
        self.name = n

    def set_surname(self, s):
        self.surname = s

    fullname = property(get_name, get_surname, set_name, set_surname)


person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)



# def pluck(data, path, default=None):
#     key_dict = path.split('.')
#     try:
#         for key in key_dict:
#             data = data[key]
#     except (KeyError, TypeError):
#         return default
#
#
# def pluck(data, path, default=None):
#     keys = path.split('.')
#     try:
#         for key in keys:
#             data = data[key]
#         return data
#     except (KeyError, TypeError):
#         return default
#
# d1 = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}
# print(pluck(d1, 'x'))
# def annual_return(start, percent, years):
#     count = start
#     for i in range(years):
#         count *= 1 + percent / 100
#         yield count
#
# for value in annual_return(120000, 10, 3):
#     print(round(value))

# import re
#
# def is_fraction(string):
#     pattern = re.compile(r'^-?\d+/\d*[1-9]\d*$')
#     return bool(pattern.fullmatch(string))

# volves = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
# pattern = [i for i, c in enumerate(input()) if c in volves]
#
# for _ in range(int(input())):
#     word = input()
#     if [i for i, c in enumerate(input()) if c in volves] == pattern:
#         print(word)


# import re
#
# def is_decimal(string):
#     try:
#         if float(string):
#             return True
#     except:
#         return False
#
#
# print(is_decimal('-199.4'))
# print(is_decimal('.-95'))
# print(is_decimal('-.95'))
# print(is_decimal('1-1'))
# def quantify(iterable, predicate):
#     res = len(list(filter(predicate, iterable)))
#     return res


# Классный пример кода

# for coords in open(0):
#     latitude, longitude = map(float, coords.strip('\n()').split(', '))
#     print(-90 <= latitude <= 90 and -180 <= longitude <= 180)



# import re
#
# def is_valid_coordinates(coord):
#     pattern = r'^\((-?\d+(\.\d+)?), (-?\d+(\.\d+)?)\)$'
#     matches = re.findall(pattern, coord)
#     for match in matches:
#         x = float(match[0])
#         y = float(match[2])
#         if -90 <= x <= 90 and -180 <= y <= 180:
#             return True
#     return False
#
# for i in open(0):
    # is_valid_coordinates(i)


# import functools
# import json
#
#
# def jsonify(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         try:
#             json_res = json.dumps(res)
#             return json_res
#         except TypeError:
#             return f'is not JSON serializable'
#     return wrapper
#
#
# @jsonify
# def make_user(id, live, options):
#     return {'id': id, 'live': live, 'options': options}
#
#
# print(make_user(4, False, None))

# from collections import Counter
# import sys
#
# pokemon_counter = Counter()
#
# for line in sys.stdin:
#     stripped_line = line.strip()
#     pokemon_counter[stripped_line] += 1
#
# duplicates_count = sum(count - 1 for count in pokemon_counter.values() if count > 1)
# print(duplicates_count)
