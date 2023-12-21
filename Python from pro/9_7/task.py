def takes_positive(func):
    def wrapper(*args, **kwargs):
        for arg in list(args, list(map(kwargs, lambda x: tuple(x)[0]))):
            if not isinstance(arg, int):
                raise TypeError(f"Argument '{arg}' is not an integer.")
            if arg <= 0:
                raise ValueError(f"Argument '{arg}' is not a positive integer.")
        return func(*args, **kwargs)
    return wrapper






# def exception_decorator(func):
#     def wrapper(*args, **kwargs):
#         try:
#             res = func(*args, **kwargs)
#             tp = (res, 'Функция выполнилась без ошибок')
#             return tp
#         except:
#             # res = func(*args, **kwargs)
#             tp = (None, 'При вызове функции произошла ошибка')
#             return tp
#     return wrapper


# sum = exception_decorator(sum)
#
# print(sum(['199', '1', 187]))




# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
#
# @do_twice
# def beegeek():
#     print('beegeek')


# print(beegeek())


# def double(func):
#     def wrapper():
#         return func() * 2
#     return wrapper
#
# @double
# def beegeek():
#     return 'beegeek'
#
# print(beegeek())