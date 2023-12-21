from collections import namedtuple

Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])

persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
           Person('Goran Aslin', 'Swedish', 'male', 1988, 0),
           Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
           Person('Genevieve Asse', 'French', 'female', 1949, 0),
           Person('Irene Adler', 'Swedish', 'female', 2005, 0),
           Person('Sergio Asti', 'Italian', 'male', 1926, 0),
           Person('Olof Backman', 'Swedish', 'male', 1999, 0),
           Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
           Person('Dana Atchley', 'American', 'female', 1941, 2000),
           Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
           Person('Shura_Stone', 'Russian', 'male', 2000, 0),
           Person('Jon Bale', 'Swedish', 'male', 2000, 0)]
gen = (i for i in persons if i.sex == 'male' and i.nationality == 'Swedish' and i.death == 0)
youngest_swedish_male = min(gen, key=lambda p: 2023 - p.birth)
print(youngest_swedish_male.name)





# def digits(number):
#     for digit in str(number):
#         yield int(digit)
#
#
# def cubed(numbers):
#     for number in numbers:
#         yield number ** 3
#
#
# def odds(numbers):
#     for number in numbers:
#         if number % 2:
#             yield number
#
#
# numbers = cubed(odds(digits(1234321)))
#
# print(*numbers)


# class BoundedRepeater:
#     def __init__(self, obj, times):
#         self.obj = obj
#         self.times = times
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.counter < self.times:
#             self.counter += 1
#             return self.obj
#         else:
#             raise StopIteration
#
# # class Repeater:
# #     def __init__(self, obj):
# #         self.obj = obj
# #
# #     def __iter__(self):
# #         return self
# #
# #     def __next__(self):
# #         return self.obj