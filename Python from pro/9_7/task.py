import functools
def takes(*allowed_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg, arg_type in zip(args, allowed_types):
                if not isinstance(arg, arg_type):
                    raise TypeError(f"Argument {arg} is not of type {arg_type.__name__}")
            return func(*args, **kwargs)

        return wrapper
    return decorator



# import functools
#
# def returns(datatype):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             if isinstance(res, datatype):
#                 return res
#             else:
#                 raise TypeError
#         return wrapper
#     return decorator


# import functools
#
# def strip_range(start, end, char=''):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res[:start] + char * (end - start) + res[end:]
#         return wrapper
#     return decorator




# import functools
#
# def repeat(times):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#
#             for i in range(1, times + 1):
#                 res = func(*args, **kwargs)
#         return wrapper
#     return decorator



# import functools
#
# def make_html(tag):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return f'<{tag}>'+func(*args, **kwargs)+f'</{tag}>'
#         return wrapper
#     return decorator




# import functools
#
# def prefix(string, to_the_end = False):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             if to_the_end:
#                 return string + res
#             else:
#                 return res + string
#
#         return wrapper
#     return decorator



# import functools
#
#
# def return_string(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if not isinstance(res, str):
#             raise TypeError()
#         return res
#
#     return wrapper

# import functools
#
#
# def square(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res ** 2
#     return wrapper

# import functools
#
# def make_capitalize(func):
#     @functools.wraps
#     def wrapper():
#         return func().capitalize()
#     return wrapper
#
# @make_capitalize
# def beegeek():
#     '''documentation'''
#     return 'beegeek'
#
# print(beegeek.__name__)
# print(beegeek.__doc__)


# def takes_positive(func):
#     def wrapper(*args, **kwargs):
#         for arg in list(args, list(map(kwargs, lambda x: tuple(x)[0]))):
#             if not isinstance(arg, int):
#                 raise TypeError(f"Argument '{arg}' is not an integer.")
#             if arg <= 0:
#                 raise ValueError(f"Argument '{arg}' is not a positive integer.")
#         return func(*args, **kwargs)
#     return wrapper


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
