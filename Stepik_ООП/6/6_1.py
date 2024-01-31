class Peekable:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def peek(self, default=None):
        if self.index >= len(self.iterable):
            if default is not None:
                return default
            else:
                raise StopIteration
        else:
            return self.iterable[self.index]

    def __iter__(self):
        return self


    def __next__(self):
        if self.index < len(self.iterable):
            result = self.iterable[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
# non_zero = filter(None, [-2, -1, 0, 1, 2])
# positive = map(abs, non_zero)
#
# print(list(non_zero))
# print(list(positive))
