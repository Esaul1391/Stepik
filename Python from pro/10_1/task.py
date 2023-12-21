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