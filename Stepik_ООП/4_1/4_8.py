from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(value):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _neg_numeric(value):
        return value * -1

    @neg.register(bool)
    @staticmethod
    def _neg_bool(value):
        return not value

print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))


# from functools import singledispatch
#
#
# class Processor:
#     @singledispatch
#     @staticmethod
#     def process(data):
#         raise TypeError('Аргумент переданного типа не поддерживается')
#
#     @process.register(int)
#     @process.register(float)
#     @staticmethod
#     def _from(data):
#         return data * 2
#
#     @process.register(str)
#     @staticmethod
#     def _from(data):
#         return data.upper()
#
#     @process.register(list)
#     @staticmethod
#     def _from(data):
#         return sorted(data)
#
#     @process.register(tuple)
#     @staticmethod
#     def _from(data):
#         return tuple(sorted(data))
#
#
# try:
#     Processor.process({1, 2, 3})
# except TypeError as e:
#     print(e)