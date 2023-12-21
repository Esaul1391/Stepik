<<<<<<< HEAD
class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.keys = list(data.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keys):
            key = self.keys[self.index]
            value = self.data[key]
            pair = (key, value)
            self.index += 1
            return pair
        else:
            raise StopIteration


# class Square:
#     def __init__(self, n):
#         self.n = n
#         self.current = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current <self.n:
#             result = self.current ** 2
#             self.current += 1
#             return result
#         else:
#             raise StopIteration


# def is_iterator(obj):
#     if '__next__' in dir(obj):
#         return True
#     else:
#         return False
#
# print(is_iterator([1, 2, 3, 4, 5]))

# numbers = [1, 2, 3, 4, 5]
#
# for i in numbers:
#     del numbers[0]
#     print(i)


# def is_iterable(obj):
#     if '__iter__' in dir(obj):
#         return True
#     else:
#         return False


# non_zero = filter(None, [-2, -1, 0, 1, 2])
# positive = map(abs, non_zero)
#
# print(list(non_zero))
# print(list(positive))


# numbers = (1, 2, 3, 4)
#
# next(numbers)
# next(numbers)
#
# print(next(numbers))
=======
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
>>>>>>> origin/main
