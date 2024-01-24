#
# def stop_on(iterable, obj):
#     for i in iterable:
#         if i == obj:
#             return
#         yield i



# from collections import Counter
# def unique(iterable):
#     for i in Counter(iterable):
#         yield i



# from collections import namedtuple
#
# Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])
#
# persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
#            Person('Goran Aslin', 'Swedish', 'male', 1988, 0),
#            Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
#            Person('Genevieve Asse', 'French', 'female', 1949, 0),
#            Person('Irene Adler', 'Swedish', 'female', 2005, 0),
#            Person('Sergio Asti', 'Italian', 'male', 1926, 0),
#            Person('Olof Backman', 'Swedish', 'male', 1999, 0),
#            Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
#            Person('Dana Atchley', 'American', 'female', 1941, 2000),
#            Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
#            Person('Shura_Stone', 'Russian', 'male', 2000, 0),
#            Person('Jon Bale', 'Swedish', 'male', 2000, 0)]
# gen = (i for i in persons if i.sex == 'male' and i.nationality == 'Swedish' and i.death == 0)
# youngest_swedish_male = min(gen, key=lambda p: 2023 - p.birth)
# print(youngest_swedish_male.name)

# def parse_ranges(ranges):
#     for r in ranges.split(','):
#         st, end = map(int, r.split('-'))
#         yield from range(st, end + 1)
#
#
#
#
# print(*parse_ranges('1-2,4-4,8-10'))