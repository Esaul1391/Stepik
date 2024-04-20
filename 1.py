from itertools import product

n = 3
m = 2

print(*product(range))



# from itertools import product
#
# def password_gen():
#     nums = range(10)
#     res = product(nums, nums, nums)
#     return res
#
# passwords = password_gen()



# from string import ascii_lowercase
# from itertools import product
#
# letters = ascii_lowercase[:8]
# digits = [1, 2, 3, 4, 5, 6, 7, 8]
#
# # for letter in letters:
# #     for digit in digits:
# #         print(letter, digit, sep='', end=' ')
#
#
# res = product(letters, digits)
# for i in res:
#     print(*i, sep='', end=' ')



# from itertools import product, combinations_with_replacement
#
#
# a = {1,2,3}
# b = {'a','b','c','d','e'}
# print(len(list(product(a, b))))
# print(*product(b, a))
# print(*product(a, a))
# print(*product(b, b))



# from itertools import combinations
#
# wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
# target = 100
# sp = set()
# count = 0
# for i in range(1, len(wallet) + 1):
#     for combo in combinations(wallet, i):
#         if sum(combo) == target:
#             sp.add(combo)
#
# print(len(sp))

# from itertools import groupby
#
#
# def ranges(numbers):
#     sorted_nums = sorted(numbers)
#     group_num = groupby(sorted_nums, key=lambda x: x - sorted_nums.index(x))
#     res = []
#     for _, i in group_num:
#         sp = list(i)
#         if len(sp) == 1:
#             res.append((sp[0], sp[0]))
#         else:
#             res.append((sp[0], sp[-1]))
#     return res


# numbers = [1, 2, 3, 4, 7, 8, 10]
#
# print(ranges(numbers))

# from  itertools import groupby
#
# def group_anagrams(words):
#     sort_words = sorted(words, key=lambda x: sorted(x))
#     group_words = groupby(sort_words, key=lambda x: sorted(x))
#     res = (tuple(l) for _, l in group_words)
#     return res
#
# groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])
#
# print(*groups)

# from itertools import groupby
#
# tasks = [('Отдых', 'поспать днем', 3),
#         ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
#         ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
#         ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
#         ('Отдых', 'погулять вечером', 4),
#         ('Курс по ооп', 'обсудить темы', 1),
#         ('Урок по groupby', 'добавить задачи на программирование', 3),
#         ('Урок по groupby', 'написать конспект', 1),
#         ('Отдых', 'погулять днем', 2),
#         ('Урок по groupby', 'добавить тестовые задачи', 2),
#         ('Уборка', 'убраться в ванной', 2),
#         ('Уборка', 'убраться в комнате', 1),
#         ('Уборка', 'убраться на кухне', 3),
#         ('Отдых', 'погулять утром', 1),
#         ('Курс по ооп', 'обсудить задачи', 2)]
#
# sort_task = sorted(tasks, key=lambda x: x[0])
# group_task = groupby(sort_task, key=lambda x: x[0])
# for i, l in group_task:
#     sp = sorted(list(l), key=lambda x: x[-1])
#     print(f'{i}:')
#     for k in sp:
#         print(f'\t{k[-1]}. {k[1]}')
#     print()


# from itertools import groupby
#
# words = 'hi never here my blue'.split()
#
# words = sorted(words, key=lambda x: len(x))
#
# res = groupby(words, key=lambda x: len(x))
# for i, l in res:
#     sp = ', '.join(i for i in sorted(list(l)))
#     print(f'{i} -> {sp}')


# from collections import namedtuple
# from itertools import groupby
#
# Student = namedtuple('Student', ['surname', 'name', 'grade'])
#
# students = [Student('Гагиев', 'Александр', 10), Student('Дедегкаев', 'Илья', 11), Student('Кодзаев', 'Георгий', 10),
#             Student('Набокова', 'Алиса', 11), Student('Кораев', 'Артур', 10), Student('Шилин', 'Александр', 11),
#             Student('Уртаева', 'Илина', 11), Student('Салбиев', 'Максим', 10), Student('Капустин', 'Илья', 11),
#             Student('Гудцев', 'Таймураз', 11), Student('Перчиков', 'Максим', 10), Student('Чен', 'Илья', 11),
#             Student('Елькина', 'Мария', 11),Student('Макоев', 'Руслан', 11), Student('Албегов', 'Хетаг', 11),
#             Student('Щербак', 'Илья', 10), Student('Идрисов', 'Баграт', 11), Student('Гапбаев', 'Герман', 10),
#             Student('Цивинская', 'Анна', 10), Student('Туткевич', 'Юрий', 11), Student('Мусиков', 'Андраник', 11),
#             Student('Гадзиев', 'Георгий', 11), Student('Белов', 'Юрий', 11), Student('Акоева', 'Диана', 11),
#             Student('Денисов', 'Илья', 11), Student('Букулова', 'Диана', 10), Student('Акоева', 'Лера', 11)]
#
# students.sort(key=lambda x: x.name)
# group_name = groupby(students, key=lambda x: x.name)
# what_max_name = max(group_name, key=lambda x: sum(1 for i in x[1]))
# print(what_max_name[0])


# from collections import namedtuple
# from itertools import groupby
#
# Person = namedtuple('Person', ['name', 'age', 'height'])
#
# persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
#            Person('Mark', 71, 172), Person('Alex', 45, 193),
#            Person('Jeff', 63, 193), Person('Ryan', 41, 184),
#            Person('Ariana', 28, 158), Person('Liam', 69, 193)]
#
# persons.sort(key=lambda x: x.height)
# res = groupby(persons, key=lambda x: x.height)
# for i, it in res:
#     res1 = ', '.join(i.name for i in list(it))
#     print(f'{i}: {res1}')

# from  itertools import zip_longest
#
#
# def grouper(iterable, n):
#     res = []
#     while len(iterable) > n:
#         res.extend(iterable[:n])
#         iterable = iterable[:n]
#     if iterable:
#         res.extend(iterable)
#     res_iter = zip_longest(*res)
#     return res_iter
#
# numbers = [1, 2, 3, 4, 5, 6]
#
# print(*grouper(numbers, 2))


# from itertools import chain, tee
#
#
# def ncycles(iterable, times):
#     res = chain.from_iterable(tee(iterable, times))
#     return res
#
# print(*ncycles([1, 2, 3, 4], 3))
