def get_min_max(data):
    if not data:
        return None
    min_index = data.index(min(data))
    max_index = data.index(max(data))
    return (min_index, max_index)


# def transpose(matrix):
#     return [list(row) for row in zip(*matrix)]

# def filterfalse(predicate, iterable):
#     if predicate is None:
#         predicate = bool
#
#     return filter(lambda x: not predicate(x), iterable)


# numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88,
#            -11, 16, -22]
# last = None
# for i in iter(numbers):
#     last = i
# print(last)

# numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88,
#            -11, 16, -22]
#
# i = iter(numbers)
# print(next(i))
# print(next(i))
# print(next(i))

# letters = map(str.upper, 'beegeek')
# numbers = filter(None, [0, 1, 2, 3])
#
# print(next(letters))
# print(next(numbers))

# beegeek = 'beegeek'
#
# iter1 = iter(beegeek)
# iter2 = iter(beegeek)
# iter3 = iter(beegeek)
#
# print(next(iter2))
# print(next(iter1))
# print(next(iter3))
#
# print(next(iter1) + next(iter2) + next(iter3))
