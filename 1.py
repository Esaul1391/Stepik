class Cycle:
    def __int__(self, iterable):
        self.iterable = iter(iterable)


cycle = Cycle('bee')

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

# from functools import partial
#
#
# to_Timur = partial(send_email, text)
# to_Timur('Тимур', 'timyrik20@beegeek.ru', 'text')
#
# send_an_invitation = partial()


# from functools import partial
#
# def multiply(a, b):
#     return a * b
#
# double = partial(multiply, 2)
# triple = partial(multiply, 3)
# print(triple(4))


# from functools import wraps
#
# class MaxRetriesException(Exception):
#     pass
# def retry(times):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             count = 0
#             while count < times:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     count += 1
#             raise MaxRetriesException
#         return wrapper
#     return decorator




# from functools import wraps
#
# def ignore_exception(*exceptions):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 return func(*args, **kwargs)
#             except exceptions as e:
#                 print(f"Исключение {type(e).__name__} обработано")
#         return wrapper
#     return decorator



# from functools import wraps
#
#
# def add_attrs(**kw):
#     def my_dec(func):
#         for k, v in kw.items():
#             func.__dict__[k] = v
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res
#
#         return wrapper
#
#     return my_dec
#
#
# @add_attrs(attr2='geek')
# @add_attrs(attr1='bee')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek.attr1)
# print(beegeek.attr2)
# print(beegeek.__dict__)
# print(help(dict.popitem))

# from functools import wraps
#
#
# def takes(*a):
#     def my_dec(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             all_arguments = args + tuple(kwargs.values())
#             for argument in all_arguments:
#                 if not isinstance(argument, a):
#                     raise TypeError
#             return res
#         return wrapper
#     return my_dec


# from functools import wraps
#
# def strip_range(start, end, char='.'):
#     def my_dec(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             span = (end - start) * char
#             if len(res) - len(res[:start]) < len(span):
#                 concat = res[:start] + (len(res) - len(res[:start])) * char
#             else:
#                 concat = res[:start] + span + res[end:]
#             return concat
#         return wrapper
#     return my_dec
#
#
# @strip_range(3, 20, '_')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())


# from functools import wraps
#
# def repeat(times):
#     def my_dec(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 func(*args, **kwargs)
#             return func
#         return wrapper
#     return my_dec


# def takes_positive(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         common = args + tuple(kwargs.values())
#         if any([not isinstance(i, int) for i in common]):
#             raise TypeError
#         elif any([i <= 0 for i in common]):
#             raise ValueError
#         return res
#     return wrapper


# from functools import wraps
#
#
# def memoized(maxsize=None):
#     def my_dec(func):
#
#         memory = {}
#         def wrapper(*args, **kwargs):
#             key = (args, tuple(sorted(kwargs.items())))
#             if key not in memory:
#                 if maxsize is None:
#                     memory[key] = func(*args, **kwargs)
#                 elif len(memory) == maxsize:
#                     memory.popitem()
#                     memory[key] = func(*args, **kwargs)
#             return memory[key]
#
#         return wrapper
#     return my_dec


# from functools import wraps
#
#
# def bucket(*a, **k):
#     def my_dec(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             bucket_args = a
#             bucket_kwargs = k
#             print((bucket_args, bucket_kwargs))
#             return res
#         return wrapper
#     return my_dec

# def  introduce_on_debug(func):
#     def wrapper(*args, **kwargs):
#         f = func(*args, **kwargs)
#
#         return f
#     return wrapper()


# def top_grade(grades: dict[str, list[int]]) -> dict[str, int]:
#
#     d = {'name': grades['name'], 'top_grade': max(grades['grades'])}
#     return d
#
# annotations = top_grade.__annotations__
#
# print(annotations['grades'])
# def get_digits(number: int | float) -> list[int]:
#     return [int(digit) for digit in str(number) if digit.isdigit()]
#
# annotations = get_digits.__annotations__
#
# print(annotations['number'])
